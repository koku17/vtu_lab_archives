#!/bin/bash

# Android stuff
BROWSER=chromium

sdkmanager () {
	sdkmanager --sdk_root=$HOME/Android/Sdk $@
}

flutter () {
	CHROME_EXECUTABLE=$BROWSER ANDROID_HOME=~/Android/Sdk flutter $@
}

# SDK version and sha256-checksum
SDK_VERSION=11076708
SDK_SUM='2d2d50857e4eb553af5a6dc3ad507a17adf43d115264b1afc116f95c92e5e258'

# Download commandline-tools and verify
wget -nc -c "https://dl.google.com/android/repository/commandlinetools-linux-${SDK_VERSION}_latest.zip"
printf "commandlinetools-linux-${SDK_VERSION}_latest.zip $SDK_SUM" | shasum -a 256 -c -

# Extract and move to ~/.local/bin
unzip commandlinetools-linux-${SDK_VERSION}_latest.zip -d ~/.local/bin

# Link in ~/.local/bin
for i in $(find ~/.local/bin/cmdline-tools/bin -maxdepth 1 -type f)
do
	ln -s "$i" ~/.local/bin/"$(basename $i)"
done

# Clone commandline-tools flutter
git clone https://github.com/flutter/flutter

# Link in ~/.local/bin
for i in $(find ~/flutter/bin/ -maxdepth 1 -executable -type f)
do
	ln -s "$i" ~/.local/bin/"$(basename $i)"
done

# Accept all licenses
yes | sdkmanager --licenses

# Install flutter sdk requierments
sdkmanager --install   \
"build-tools;28.0.3"   \
"platforms;android-29" \
"cmdline-tools;latest" \
"platform-tools"

# Verify Flutter installation
flutter doctor -v
