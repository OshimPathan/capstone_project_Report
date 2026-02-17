# 🚀 Making Rebirth Live: Frontend Deployment Guide

Since your **Backend is already live** at `https://rebirth-backend-zeta.vercel.app/api`, the next step is to deploy your **Frontend (Mobile App & Web App)** so users can access it.

---

## 1. ✅ Verify Connection
Before deploying, ensure your app is pointing to the live backend.
- Opens `lib/services/auth_service.dart`.
- Confirm `_baseUrl` is set to your Vercel URL (Completed).

---

## 2. 🌐 Option A: Deploy as a Web App (Easiest & Fastest)
This allows anyone with a browser to use your app instantly.

### Step 1: Build for Web
Run this command in your terminal:
```bash
cd rebirth
flutter build web --release --web-renderer html
```
*Note: `--web-renderer html` ensures better compatibility across devices.*

### Step 2: Deploy to Vercel
1.  Go to [Vercel Dashboard](https://vercel.com/dashboard).
2.  Click **Add New Project** -> Select your Git Repository (`capstone_project_Report`).
3.  **Configure Project**:
    - **Framework Preset**: Select "Other".
    - **Root Directory**: Select `rebirth`.
    - **Build Command**: `flutter build web --release`
    - **Output Directory**: `build/web`
4.  Click **Deploy**.

🎉 **Result**: You will get a URL like `https://rebirth-frontend.vercel.app`.

---

## 3. 📱 Option B: Release Android App (APK)
For users who want to install it on their phones.

### Step 1: Build APK
Run this command:
```bash
cd rebirth
flutter build apk --release
```

### Step 2: Locate the File
The APK file will be generated at:
`rebirth/build/app/outputs/flutter-apk/app-release.apk`

### Step 3: Distribute
1.  Go to your GitHub Repository.
2.  Click on **Releases** (right sidebar) -> **Draft a new release**.
3.  Tag version `v1.0.0`.
4.  Upload the `app-release.apk` file.
5.  Click **Publish release**.

Users can now download and install the app directly from GitHub!

---

## 4. 🍎 Option C: iOS (Mac Required)
1.  Open `rebirth/ios/Runner.xcworkspace` in Xcode.
2.  Select your Development Team in Signing & Capabilities.
3.  Go to **Product** -> **Archive**.
4.  Distribute via TestFlight or Ad-hoc.

---

## 🔗 Summary
- **Backend**: Live on Vercel (Done).
- **Frontend**: Recommend deploying the Web version first for instant access.
