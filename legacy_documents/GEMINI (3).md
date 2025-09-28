## Project Overview

This is a minimal Android WebView app designed to display a specific web page, `https://www.empiricontario.com/presentation_2/`, in a full-screen, immersive mode. The application is built using Kotlin and Gradle, and it's intended for quick deployment to an Android device.

The core functionality of the app is to load a predefined URL in a WebView, with features like pull-to-refresh, zoom, and JavaScript enabled. It also handles back-button navigation within the WebView's history and opens external links in the device's default browser.

The project includes shell scripts to streamline the setup of the development environment, as well as building and running the application.

## Building and Running

### Prerequisites

*   An Android device with Developer options and USB debugging enabled.
*   Windows Subsystem for Linux (WSL) is recommended for running the provided scripts.

### Quickstart

1.  **Install Android Tools:**
    *   Run the `scripts/install_android_tools.sh` script to install Java 17, Gradle, and the Android SDK command-line tools.
    *   This script will also provide you with the necessary environment variables to set in your shell's configuration file (e.g., `~/.bashrc`).

2.  **Generate Gradle Wrapper:**
    *   Run `gradle wrapper` to generate the Gradle wrapper scripts.

3.  **Build the Debug APK:**
    *   Execute the `scripts/build_debug.sh` script to build the debug version of the Android application (APK).

4.  **Run on Device:**
    *   Connect your Android device via USB.
    *   Run the `scripts/run_on_device.sh` script to install and launch the app on your device.

### Configuration

The starting URL can be configured in two ways:

1.  **Hardcoded:**
    *   Modify the `START_URL` constant in `app/src/main/java/com/empiric/webnavigator/MainActivity.kt`.

2.  **Build Time:**
    *   Use a Gradle property when building the app:
        ```bash
        ./gradlew assembleDebug -Papp.startUrl="https://example.com"
        ```

## Development Conventions

*   **Language:** The application is written in Kotlin.
*   **Build Tool:** Gradle is used for building the project.
*   **Project Structure:** The project follows the standard Android application structure.
*   **Scripts:** Shell scripts are provided for automating common development tasks.
*   **Min SDK:** The minimum supported Android SDK version is 24 (Android 7.0).
*   **Target SDK:** The target Android SDK version is 34.
