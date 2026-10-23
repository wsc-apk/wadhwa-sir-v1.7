#!/usr/bin/env bash
set -euo pipefail
KIND="${1:?Expected apk or aab}"
EXPECTED="AEDD5EB699AA7F9B1C2F2D6DB88651D153C69F3AEA73D815AB4D5B7462DEEC23"
for name in WSC_KEYSTORE_PASSWORD WSC_KEY_PASSWORD WSC_KEY_ALIAS; do
  [[ -n "${!name:-}" ]] || { echo "::error::Missing secret $name"; exit 1; }
done
mkdir -p release
CERT="$(mktemp)"
trap 'rm -f "$CERT"' EXIT
keytool -exportcert -rfc -keystore upload-keystore.jks -storepass:env WSC_KEYSTORE_PASSWORD -alias "$WSC_KEY_ALIAS" -file "$CERT"
ACTUAL="$(openssl x509 -in "$CERT" -noout -fingerprint -sha256 | cut -d= -f2 | tr -d ':\r\n ' | tr '[:lower:]' '[:upper:]')"
[[ "$ACTUAL" == "$EXPECTED" ]] || { echo '::error::Wrong upload certificate'; exit 1; }
BT="$ANDROID_HOME/build-tools/36.0.0"
if [[ "$KIND" == apk ]]; then
  SOURCE=android/app/build/outputs/apk/release/app-release-unsigned.apk
  [[ -f "$SOURCE" ]] || { echo '::error::Unsigned release APK not found'; exit 1; }
  "$BT/zipalign" -P 16 -f 4 "$SOURCE" "$RUNNER_TEMP/aligned.apk"
  "$BT/apksigner" sign --ks upload-keystore.jks --ks-pass env:WSC_KEYSTORE_PASSWORD --key-pass env:WSC_KEY_PASSWORD --ks-key-alias "$WSC_KEY_ALIAS" --out release/WSC-1.7-17-signed.apk "$RUNNER_TEMP/aligned.apk"
  "$BT/apksigner" verify --verbose --print-certs release/WSC-1.7-17-signed.apk > release/signature-report.txt
  CERT_DIGEST="$(sed -n 's/^Signer #1 certificate SHA-256 digest: //p' release/signature-report.txt | tr -d ':\r\n ' | tr '[:lower:]' '[:upper:]')"
  [[ "$CERT_DIGEST" == "$EXPECTED" ]] || { echo '::error::Final APK signer mismatch'; exit 1; }
  "$BT/aapt" dump badging release/WSC-1.7-17-signed.apk > release/package-report.txt
  grep -q "name='com.wadhwasir.classroom' versionCode='17' versionName='1.7'" release/package-report.txt
  grep -q "targetSdkVersion:'36'" release/package-report.txt
  grep -q 'com.google.android.gms.permission.AD_ID' release/package-report.txt
elif [[ "$KIND" == aab ]]; then
  cp android/app/build/outputs/bundle/release/app-release.aab release/WSC-1.7-17-signed.aab
  jarsigner -J-Duser.language=en -J-Duser.country=US -keystore upload-keystore.jks -storepass:env WSC_KEYSTORE_PASSWORD -keypass:env WSC_KEY_PASSWORD release/WSC-1.7-17-signed.aab "$WSC_KEY_ALIAS"
  jarsigner -J-Duser.language=en -J-Duser.country=US -verify release/WSC-1.7-17-signed.aab > release/signature-report.txt 2>&1
  grep -q 'jar verified\.' release/signature-report.txt
  keytool -J-Duser.language=en -J-Duser.country=US -printcert -jarfile release/WSC-1.7-17-signed.aab > release/certificate-report.txt
  CERT_DIGEST="$(sed -n 's/.*SHA256: //p' release/certificate-report.txt | head -1 | tr -d ':\r\n ' | tr '[:lower:]' '[:upper:]')"
  [[ "$CERT_DIGEST" == "$EXPECTED" ]] || { echo '::error::Final AAB signer mismatch'; exit 1; }
  curl --fail --location --retry 3 https://github.com/google/bundletool/releases/download/1.18.2/bundletool-all-1.18.2.jar --output "$RUNNER_TEMP/bundletool.jar"
  java -jar "$RUNNER_TEMP/bundletool.jar" validate --bundle=release/WSC-1.7-17-signed.aab
  java -jar "$RUNNER_TEMP/bundletool.jar" dump manifest --bundle=release/WSC-1.7-17-signed.aab --module=base > release/manifest.xml
  python3 - <<'PY'
import xml.etree.ElementTree as ET
r=ET.parse('release/manifest.xml').getroot(); a='{http://schemas.android.com/apk/res/android}'
assert r.get('package')=='com.wadhwasir.classroom'
assert r.get(a+'versionCode')=='17' and r.get(a+'versionName')=='1.7'
assert r.find('uses-sdk').get(a+'targetSdkVersion')=='36'
assert any(e.get(a+'name')=='com.google.android.gms.permission.AD_ID' for e in r.findall('uses-permission'))
PY
else
  echo '::error::Unknown artifact type'; exit 1
fi
cp android/app/build/outputs/mapping/release/mapping.txt release/mapping.txt
printf '\n## Verified WSC release\n- Package: com.wadhwasir.classroom\n- Version: 1.7 / 17\n- Target SDK: 36\n- AD_ID permission: present\n- Final artifact signature: verified\n- Upload certificate: matched\n- Format: %s\n- Play acceptance and runtime behaviour still require testing.\n' "$KIND" >> "$GITHUB_STEP_SUMMARY"
