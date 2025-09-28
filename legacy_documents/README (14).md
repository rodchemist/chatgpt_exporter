# EmpiricWebNavigator

A minimal Android WebView app that opens `https://www.empiricontario.com/presentation_2/`. Designed for quick phone deployment.
Includes scripts to install Android tooling on WSL/Windows 11 and to build/run the app.

---

## 1) Repository Layout

```
empiric-phone-webnavigator/
├── app/                         # Android app module
│   ├── build.gradle.kts
│   └── src/main/...
├── build.gradle.kts
├── settings.gradle.kts
├── gradle.properties
├── scripts/
│   ├── install_android_tools.sh
│   ├── build_debug.sh
│   └── run_on_device.sh
├── .gitignore
└── README.md
```

## 2) Quickstart (WSL Ubuntu)

> ⚠️ Emulators in WSL are tricky. Prefer a **real Android phone** via USB or **ADB over Wi‑Fi**.

```bash
# Clone and enter
git clone <your-repo-url> empiric-phone-webnavigator
cd empiric-phone-webnavigator

# 1) Install Android tools (Java 17, Gradle, Android SDK CLI)
bash scripts/install_android_tools.sh

# 2) Set environment variables in your shell
# (the installer prints the exact lines to add to ~/.bashrc; re-open your shell after adding)

# 3) Generate Gradle wrapper (uses system Gradle installed by the script)
gradle wrapper

# 4) Build debug APK
bash scripts/build_debug.sh

# 5) Connect a device (USB or Wi‑Fi) and install
bash scripts/run_on_device.sh
```

### ADB over Wi‑Fi (optional)

On your Android phone (same network):
1. Enable **Developer options** → **Wireless debugging**.
2. Pair the device and note the IP+port, then:
```bash
adb connect <PHONE_IP>:<PORT>
adb devices     # should list your device
```

If using Windows for ADB instead of WSL, you can still build inside WSL and then `adb connect` from Windows PowerShell.

## 3) App Behavior

- Loads `https://www.empiricontario.com/presentation_2/` with a full‑screen WebView.
- Pull‑to‑refresh.
- Zoom enabled; caching enabled; JS enabled.
- Handles the Android back button to navigate WebView history.
- Opens external URLs (non-http/https or off-domain) in the default browser.

## 4) Configuration

Update the URL in **`app/src/main/java/com/empiric/webnavigator/MainActivity.kt`** or via a gradle property:
- To hardcode another URL, change the `START_URL` constant.
- To inject at build time: `./gradlew assembleDebug -Papp.startUrl="https://example.com"`

## 5) Notes

- Min SDK 24 (Android 7.0); Target SDK 34.
- Network connectivity is required to load the site.
- For best performance, ensure the target site uses HTTPS and mobile‑friendly layout.
