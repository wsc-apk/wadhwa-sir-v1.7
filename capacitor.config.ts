import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.wadhwasir.classroom',
  appName: 'WADHWA SIR CLASSROOM',
  webDir: 'www',
  backgroundColor: '#0a0f1c',
  server: {
    url: 'https://wsc-apk.netlify.app',
    cleartext: false,
    androidScheme: 'https',
    allowNavigation: ['wsc-apk.netlify.app']
  },
  plugins: {
    SystemBars: { insetsHandling: 'disable' },
    SplashScreen: {
      launchShowDuration: 0,
      launchAutoHide: true,
      backgroundColor: '#0a0f1c',
      androidSplashResourceName: 'splash',
      showSpinner: false
    },
    PushNotifications: { presentationOptions: ['badge', 'sound', 'alert'] }
  }
};
export default config;
