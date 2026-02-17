# 🚀 Deployment Guide: Making "Rebirth" Live

This guide explains how to deploy both the Flutter Frontend (Web/Mobile) and the Node.js Backend to make your project live for users.

---

## 1. 🖥️ Backend Deployment (Node.js API)

We will use **Vercel** for the backend as it's free, fast, and already configured in your project (`vercel.json`).

### Steps:
1.  **Push to GitHub**: Ensure your latest backend code is on GitHub (already done).
2.  **Login to Vercel**: Go to [vercel.com](https://vercel.com) and sign up/login with GitHub.
3.  **Import Project**:
    - Click **"Add New Project"**.
    - Select your repository: `capstone_project_Report`.
    - Set the **Root Directory** to `rebirth_backend/rebirth-backend`.
4.  **Environment Variables**:
    - Add the following variables from your local `.env`:
      - `MONGODB_URI`: Your MongoDB Atlas connection string.
      - `JWT_SECRET`: Your secret key.
      - `GEMINI_API_KEY`: Your Google Gemini API key.
      - `HUGGINGFACE_API_KEY`: Your Hugging Face API key.
5.  **Deploy**: Click **"Deploy"**.
6.  **Get URL**: Once done, Vercel will give you a domain (e.g., `https://rebirth-backend.vercel.app`).
    - **Update Frontend**: Go to `rebirth/lib/services/api_service.dart` (or equivalent) and replace `localhost:3000` with this new URL.

---

## 2. 📱 Frontend Deployment

You have two options: **Web App** (easiest for demos) or **Mobile App** (APK/IPA).

### Option A: Web App (Recommended for Demos)
Your project is now web-enabled!

1.  **Build for Web**:
    Run this command in your terminal:
    ```bash
    cd rebirth
    flutter build web --release
    ```
2.  **Deploy to Vercel/Netlify**:
    - The build files will be in `rebirth/build/web`.
    - **Manual**: Drag and drop the `build/web` folder into [Netlify Drop](https://app.netlify.com/drop).
    - **Automatic (Vercel)**:
        - In Vercel, import the same repo again.
        - Set **Root Directory** to `rebirth`.
        - Set **Build Command**: `flutter build web --release`
        - Set **Output Directory**: `build/web`
        - Click **Deploy**.

### Option B: Android APK (For Mobile Users)
1.  **Build APK**:
    Run this command in your terminal:
    ```bash
    cd rebirth
    flutter build apk --release
    ```
2.  **Locate File**: The APK will be at `rebirth/build/app/outputs/flutter-apk/app-release.apk`.
3.  **Distribute**:
    - **GitHub Releases**: Go to your repo -> "Releases" -> "Draft a new release" -> Upload the `.apk` file.
    - **Google Drive**: Upload and share the link.

---

## 3. 🗄️ Database (MongoDB Atlas)

Ensure your database is accessible from the cloud:
1.  Go to [MongoDB Atlas](https://cloud.mongodb.com).
2.  Navigate to **Network Access**.
3.  Ensure IP Access List includes `0.0.0.0/0` (Allow Access from Anywhere) so Vercel can connect.

---

## ✅ Summary Checklist

- [ ] Backend deployed to Vercel.
- [ ] Backend URL updated in Flutter `api_service.dart`.
- [ ] MongoDB Network Access set to `0.0.0.0/0`.
- [ ] Flutter Web built & deployed OR APK generated & uploaded to GitHub Releases.

🚀 **Your project is now live!**
