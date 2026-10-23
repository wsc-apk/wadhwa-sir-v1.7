GENERATED = {'app/src/main/java/com/wadhwasir/classroom/MainActivity.java': 'package com.wadhwasir.classroom;\n'
                                                                '\n'
                                                                'import android.os.Bundle;\n'
                                                                'import android.view.View;\n'
                                                                'import androidx.core.graphics.Insets;\n'
                                                                'import androidx.core.view.ViewCompat;\n'
                                                                'import androidx.core.view.WindowCompat;\n'
                                                                'import '
                                                                'androidx.core.view.WindowInsetsCompat;\n'
                                                                'import '
                                                                'androidx.core.view.WindowInsetsControllerCompat;\n'
                                                                'import com.getcapacitor.BridgeActivity;\n'
                                                                '\n'
                                                                'public class MainActivity extends '
                                                                'BridgeActivity {\n'
                                                                '    @Override public void onCreate(Bundle '
                                                                'savedInstanceState) {\n'
                                                                '        '
                                                                'registerPlugin(WSCNativePlugin.class);\n'
                                                                '        '
                                                                'super.onCreate(savedInstanceState);\n'
                                                                '        '
                                                                'WindowCompat.setDecorFitsSystemWindows(getWindow(), '
                                                                'false);\n'
                                                                '        View root = '
                                                                'findViewById(android.R.id.content);\n'
                                                                '        '
                                                                'ViewCompat.setOnApplyWindowInsetsListener(root, '
                                                                '(view, windowInsets) -> {\n'
                                                                '            Insets safe = '
                                                                'windowInsets.getInsets(WindowInsetsCompat.Type.navigationBars() '
                                                                '| '
                                                                'WindowInsetsCompat.Type.displayCutout());\n'
                                                                '            Insets keyboard = '
                                                                'windowInsets.getInsets(WindowInsetsCompat.Type.ime());\n'
                                                                '            view.setPadding(safe.left, '
                                                                'safe.top, safe.right, Math.max(safe.bottom, '
                                                                'keyboard.bottom));\n'
                                                                '            return windowInsets;\n'
                                                                '        });\n'
                                                                '        '
                                                                'ViewCompat.requestApplyInsets(root);\n'
                                                                '        hideStatusBar();\n'
                                                                '    }\n'
                                                                '    private void hideStatusBar() {\n'
                                                                '        WindowInsetsControllerCompat '
                                                                'controller =\n'
                                                                '            '
                                                                'WindowCompat.getInsetsController(getWindow(), '
                                                                'getWindow().getDecorView());\n'
                                                                '        controller.setSystemBarsBehavior(\n'
                                                                '            '
                                                                'WindowInsetsControllerCompat.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE);\n'
                                                                '        '
                                                                'controller.hide(WindowInsetsCompat.Type.statusBars());\n'
                                                                '    }\n'
                                                                '    @Override public void '
                                                                'onWindowFocusChanged(boolean hasFocus) {\n'
                                                                '        '
                                                                'super.onWindowFocusChanged(hasFocus);\n'
                                                                '        if (hasFocus) hideStatusBar();\n'
                                                                '    }\n'
                                                                '}\n',
 'app/src/main/java/com/wadhwasir/classroom/WscApplication.java': 'package com.wadhwasir.classroom;\n'
                                                                  '\n'
                                                                  'import android.app.Application;\n'
                                                                  'import com.google.firebase.FirebaseApp;\n'
                                                                  'import '
                                                                  'com.google.firebase.appcheck.FirebaseAppCheck;\n'
                                                                  'import '
                                                                  'com.google.firebase.appcheck.playintegrity.PlayIntegrityAppCheckProviderFactory;\n'
                                                                  'import '
                                                                  'com.google.firebase.analytics.FirebaseAnalytics;\n'
                                                                  'import '
                                                                  'com.google.firebase.crashlytics.FirebaseCrashlytics;\n'
                                                                  '\n'
                                                                  'public class WscApplication extends '
                                                                  'Application {\n'
                                                                  '    @Override public void onCreate() {\n'
                                                                  '        super.onCreate();\n'
                                                                  '        FirebaseApp.initializeApp(this);\n'
                                                                  '        '
                                                                  'FirebaseAppCheck.getInstance().installAppCheckProviderFactory(\n'
                                                                  '            '
                                                                  'PlayIntegrityAppCheckProviderFactory.getInstance());\n'
                                                                  '        '
                                                                  'FirebaseAnalytics.getInstance(this);\n'
                                                                  '        '
                                                                  'FirebaseCrashlytics.getInstance().setCustomKey("wsc_release", '
                                                                  '"1.7");\n'
                                                                  '    }\n'
                                                                  '}\n',
 'app/src/main/java/com/wadhwasir/classroom/WSCNativePlugin.java': 'package com.wadhwasir.classroom;\n'
                                                                   '\n'
                                                                   'import android.net.Uri;\n'
                                                                   'import android.os.Bundle;\n'
                                                                   'import com.getcapacitor.JSObject;\n'
                                                                   'import com.getcapacitor.Plugin;\n'
                                                                   'import com.getcapacitor.PluginCall;\n'
                                                                   'import com.getcapacitor.PluginMethod;\n'
                                                                   'import '
                                                                   'com.getcapacitor.annotation.CapacitorPlugin;\n'
                                                                   'import '
                                                                   'com.google.firebase.analytics.FirebaseAnalytics;\n'
                                                                   'import '
                                                                   'com.google.firebase.appcheck.FirebaseAppCheck;\n'
                                                                   'import '
                                                                   'com.google.firebase.crashlytics.FirebaseCrashlytics;\n'
                                                                   '\n'
                                                                   '@CapacitorPlugin(name = "WSCNative")\n'
                                                                   'public class WSCNativePlugin extends '
                                                                   'Plugin {\n'
                                                                   '    private boolean trusted(PluginCall '
                                                                   'call) {\n'
                                                                   '        // Only the owned HTTPS site may '
                                                                   'use the Firebase bridge.\n'
                                                                   '        String url = '
                                                                   'getBridge().getWebView().getUrl();\n'
                                                                   '        Uri uri = url == null ? '
                                                                   'Uri.EMPTY : Uri.parse(url);\n'
                                                                   '        if '
                                                                   '(!"https".equals(uri.getScheme()) || '
                                                                   '!"wsc-apk.netlify.app".equals(uri.getHost())) '
                                                                   '{\n'
                                                                   '            call.reject("Native Firebase '
                                                                   'is restricted to the WSC HTTPS site.");\n'
                                                                   '            return false;\n'
                                                                   '        }\n'
                                                                   '        return true;\n'
                                                                   '    }\n'
                                                                   '    @PluginMethod public void '
                                                                   'getStatus(PluginCall call) {\n'
                                                                   '        getActivity().runOnUiThread(() '
                                                                   '-> {\n'
                                                                   '        if (!trusted(call)) return;\n'
                                                                   '        JSObject out = new JSObject();\n'
                                                                   '        out.put("versionName", '
                                                                   'BuildConfig.VERSION_NAME);\n'
                                                                   '        out.put("versionCode", '
                                                                   'BuildConfig.VERSION_CODE);\n'
                                                                   '        out.put("provider", '
                                                                   '"play-integrity");\n'
                                                                   '        out.put("crashlytics", true);\n'
                                                                   '        call.resolve(out);\n'
                                                                   '            });\n'
                                                                   '    }\n'
                                                                   '    @PluginMethod public void '
                                                                   'getAppCheckToken(PluginCall call) {\n'
                                                                   '        getActivity().runOnUiThread(() '
                                                                   '-> {\n'
                                                                   '        if (!trusted(call)) return;\n'
                                                                   '        '
                                                                   'FirebaseAppCheck.getInstance().getAppCheckToken(false)\n'
                                                                   '            .addOnSuccessListener(result '
                                                                   '-> {\n'
                                                                   '                JSObject out = new '
                                                                   'JSObject();\n'
                                                                   '                out.put("token", '
                                                                   'result.getToken());\n'
                                                                   '                '
                                                                   'out.put("expireTimeMillis", '
                                                                   'result.getExpireTimeMillis());\n'
                                                                   '                call.resolve(out);\n'
                                                                   '            '
                                                                   '}).addOnFailureListener(error -> '
                                                                   'call.reject("Play Integrity attestation '
                                                                   'failed. Verify Play distribution and App '
                                                                   'Check registration.", error));\n'
                                                                   '            });\n'
                                                                   '    }\n'
                                                                   '    @PluginMethod public void '
                                                                   'logScreen(PluginCall call) {\n'
                                                                   '        getActivity().runOnUiThread(() '
                                                                   '-> {\n'
                                                                   '        if (!trusted(call)) return;\n'
                                                                   '        String screen = '
                                                                   'call.getString("screen", "home");\n'
                                                                   '        // Screen identifiers only. '
                                                                   'Never send form input or full URLs.\n'
                                                                   '        screen = '
                                                                   'screen.replaceAll("[^a-zA-Z0-9_.:/-]", '
                                                                   '"_");\n'
                                                                   '        if (screen.length() > 100) '
                                                                   'screen = screen.substring(0, 100);\n'
                                                                   '        Bundle data = new Bundle();\n'
                                                                   '        '
                                                                   'data.putString(FirebaseAnalytics.Param.SCREEN_NAME, '
                                                                   'screen);\n'
                                                                   '        '
                                                                   'data.putString(FirebaseAnalytics.Param.SCREEN_CLASS, '
                                                                   '"WSCWebView");\n'
                                                                   '        '
                                                                   'FirebaseAnalytics.getInstance(getContext()).logEvent(FirebaseAnalytics.Event.SCREEN_VIEW, '
                                                                   'data);\n'
                                                                   '        call.resolve();\n'
                                                                   '            });\n'
                                                                   '    }\n'
                                                                   '    @PluginMethod public void '
                                                                   'logTestEvent(PluginCall call) {\n'
                                                                   '        getActivity().runOnUiThread(() '
                                                                   '-> {\n'
                                                                   '        if (!trusted(call)) return;\n'
                                                                   '        '
                                                                   'FirebaseAnalytics.getInstance(getContext()).logEvent("wsc_native_test", '
                                                                   'new Bundle());\n'
                                                                   '        call.resolve();\n'
                                                                   '            });\n'
                                                                   '    }\n'
                                                                   '    @PluginMethod public void '
                                                                   'recordTestException(PluginCall call) {\n'
                                                                   '        getActivity().runOnUiThread(() '
                                                                   '-> {\n'
                                                                   '        if (!trusted(call)) return;\n'
                                                                   '        '
                                                                   'FirebaseCrashlytics.getInstance().recordException(\n'
                                                                   '            new RuntimeException("WSC '
                                                                   '1.7 user-triggered nonfatal diagnostic '
                                                                   'test"));\n'
                                                                   '        call.resolve();\n'
                                                                   '            });\n'
                                                                   '    }\n'
                                                                   '}\n',
 'app/build.gradle': "apply plugin: 'com.android.application'\n"
                     "apply plugin: 'com.google.gms.google-services'\n"
                     "apply plugin: 'com.google.firebase.crashlytics'\n"
                     '\n'
                     'android {\n'
                     "    namespace = 'com.wadhwasir.classroom'\n"
                     '    compileSdk = 36\n'
                     '    defaultConfig {\n'
                     "        applicationId 'com.wadhwasir.classroom'\n"
                     '        minSdkVersion 24\n'
                     '        targetSdkVersion 36\n'
                     '        versionCode 17\n'
                     "        versionName '1.7'\n"
                     "        testInstrumentationRunner 'androidx.test.runner.AndroidJUnitRunner'\n"
                     '        aaptOptions {\n'
                     '            ignoreAssetsPattern = '
                     "'!.svn:!.git:!.ds_store:!*.scc:.*:!CVS:!thumbs.db:!picasa.ini:!*~'\n"
                     '        }\n'
                     '    }\n'
                     '    buildFeatures { buildConfig = true }\n'
                     '    buildTypes {\n'
                     '        release {\n'
                     '            minifyEnabled true\n'
                     '            shrinkResources true\n'
                     "            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), "
                     "'proguard-rules.pro'\n"
                     '            firebaseCrashlytics { mappingFileUploadEnabled true }\n'
                     '        }\n'
                     '    }\n'
                     '}\n'
                     'repositories {\n'
                     "    flatDir { dirs '../capacitor-cordova-android-plugins/src/main/libs', 'libs' }\n"
                     '}\n'
                     'dependencies {\n'
                     "    implementation fileTree(include: ['*.jar'], dir: 'libs')\n"
                     '    implementation "androidx.appcompat:appcompat:$androidxAppCompatVersion"\n'
                     '    implementation '
                     '"androidx.coordinatorlayout:coordinatorlayout:$androidxCoordinatorLayoutVersion"\n'
                     '    implementation "androidx.core:core-splashscreen:$coreSplashScreenVersion"\n'
                     "    implementation project(':capacitor-android')\n"
                     "    implementation project(':capacitor-cordova-android-plugins')\n"
                     "    implementation platform('com.google.firebase:firebase-bom:34.7.0')\n"
                     "    implementation 'com.google.firebase:firebase-analytics'\n"
                     "    implementation 'com.google.firebase:firebase-crashlytics'\n"
                     "    implementation 'com.google.firebase:firebase-appcheck-playintegrity'\n"
                     '}\n'
                     "apply from: 'capacitor.build.gradle'\n",
 'app/proguard-rules.pro': '# WSC-R8-PERMISSIONS-FIX-1\n'
                           '# Capacitor reads these annotation TYPES via reflection. Keeping only annotated\n'
                           '# plugin classes and annotation attributes is insufficient in R8 full mode.\n'
                           '# Matches the Capacitor 8 fix in ionic-team/capacitor PR #8646 / issue #8589.\n'
                           '-keep @interface com.getcapacitor.annotation.** { *; }\n'
                           '-keep @interface com.getcapacitor.PluginMethod { *; }\n'
                           '-keep @interface com.getcapacitor.NativePlugin { *; }\n'
                           '\n'
                           "# Keep Capacitor's reflection-discovered plugin entry points, not all app code.\n"
                           '-keepattributes '
                           'Signature,InnerClasses,EnclosingMethod,*Annotation*,SourceFile,LineNumberTable\n'
                           '-keep @com.getcapacitor.annotation.CapacitorPlugin class * { *; }\n'
                           '-keepclassmembers class * {\n'
                           '    @com.getcapacitor.PluginMethod <methods>;\n'
                           '    @android.webkit.JavascriptInterface <methods>;\n'
                           '}\n'}

from pathlib import Path
import json, shutil, xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
A = ROOT / 'android'
if not (A / 'app/build.gradle').exists():
    raise SystemExit('Android project missing. Run cap add and cap sync first.')
config = json.loads((ROOT / 'google-services.json').read_text())
assert config['project_info']['project_id'] == 'wadhwa-sir-classroom', 'Wrong Firebase project'
assert any(c['client_info'].get('android_client_info', {}).get('package_name') == 'com.wadhwasir.classroom' for c in config['client']), 'Wrong Firebase Android package'
shutil.copy2(ROOT / 'google-services.json', A / 'app/google-services.json')
for relative, contents in GENERATED.items():
    destination = A / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(contents)

build = A / 'build.gradle'
s = build.read_text()
needle = "classpath 'com.google.gms:google-services:4.4.4'"
assert needle in s, 'Unexpected Capacitor template: Google Services plugin line changed'
s = s.replace(needle, needle + "\n        classpath 'com.google.firebase:firebase-crashlytics-gradle:3.0.6'")
build.write_text(s)
variables = A / 'variables.gradle'
s = variables.read_text()
assert 'compileSdkVersion = 36' in s and 'targetSdkVersion = 36' in s
s = s.replace('ext {', "ext {\n    playServicesAdsVersion = '24.9.0'\n    userMessagingPlatformVersion = '4.0.0'", 1)
variables.write_text(s)
props = A / 'gradle.properties'
props.write_text(props.read_text() + '\nandroid.r8.optimizedResourceShrinking=true\n')

ns = 'http://schemas.android.com/apk/res/android'
ET.register_namespace('android', ns)
manifest = A / 'app/src/main/AndroidManifest.xml'
tree = ET.parse(manifest)
root = tree.getroot()
attr = lambda key: '{' + ns + '}' + key
for permission in ['android.permission.INTERNET', 'com.google.android.gms.permission.AD_ID']:
    if not any(e.get(attr('name')) == permission for e in root.findall('uses-permission')):
        ET.SubElement(root, 'uses-permission', {attr('name'): permission})
app = root.find('application')
app.set(attr('name'), '.WscApplication')
metadata = {
    'com.google.android.gms.ads.APPLICATION_ID': 'ca-app-pub-8576378038310405~4113931989',
    'google_analytics_automatic_screen_reporting_enabled': 'false',
    'google_analytics_default_allow_ad_personalization_signals': 'false'
}
for name, value in metadata.items():
    element = next((e for e in app.findall('meta-data') if e.get(attr('name')) == name), None)
    if element is None: element = ET.SubElement(app, 'meta-data')
    element.set(attr('name'), name)
    element.set(attr('value'), value)
tree.write(manifest, encoding='utf-8', xml_declaration=True)
assert any(e.get(attr('name')) == 'com.google.android.gms.permission.AD_ID' for e in root.findall('uses-permission'))
print('PASS: version 1.7/code 17, SDK 36, AD_ID, AdMob ID, native Firebase, immersive status bar and R8 configured.')

print("PASS: WSC-R8-PERMISSIONS-FIX-1 annotation keep rules included; device retest required.")
