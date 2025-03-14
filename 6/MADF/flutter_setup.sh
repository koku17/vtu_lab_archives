#!/bin/bash

sdkmanager () {
	~/.local/bin/sdkmanager --sdk_root=$HOME/Android/Sdk $@
}

die () {
	echo -e "\e[31m$1\e[0m"
	exit $2
}

success () {
	echo -e "\e[32m$1\e[0m"
	return $2
}

# Browser
BROWSWER=chrome

# SDK version and sha256-checksum
SDK_VERSION=11076708
SDK_SUM='2d2d50857e4eb553af5a6dc3ad507a17adf43d115264b1afc116f95c92e5e258'

# Download commandline-tools and verify
wget -nc -c "https://dl.google.com/android/repository/commandlinetools-linux-${SDK_VERSION}_latest.zip" \
	-O ~/"commandlinetools-linux-${SDK_VERSION}_latest.zip"
printf "$SDK_SUM  $HOME/commandlinetools-linux-${SDK_VERSION}_latest.zip" | shasum -a 256 -c - && \
success "File verified successfully" "0" || \
(
	die "Download corrupted try again" "-1"
)

# Extract and move to ~/.local/bin and link in ~/.local/bin
[ -d ~/.local/bin/cmdline-tools ] || \
(
	echo "Unzipping ..."
	unzip commandlinetools-linux-${SDK_VERSION}_latest.zip -d ~/.local/bin
	echo "Linking to cmdline-tools binaries ~/.local/bin ..."
	for i in $(find ~/.local/bin/cmdline-tools/bin -maxdepth 1 -type f)
	do
		ln -s "$i" ~/.local/bin/"$(basename $i)"
	done
)

# Clone commandline-tools flutter
[ -d ~/flutter ] || git clone https://github.com/flutter/flutter

# Link in ~/.local/bin
[ -f ~/.local/bin/flutter ] || \
(
	echo "Linking flutter binaries to ~/.local/bin ..."
	for i in $(find ~/flutter/bin/ -maxdepth 1 -executable -type f)
	do
		ln -s "$i" ~/.local/bin/"$(basename $i)"
	done
)

# Accept all licenses
echo "Accepting SDK Licenses ..."
yes | sdkmanager --licenses 1>&2> /dev/null && \
success "All SDK licenses are accepted" || \
die "All SDK licenses are not accepted !"


# Install flutter sdk requierments
echo "Installing android requierements ..."
sdkmanager --install   \
"build-tools;28.0.3"   \
"platforms;android-29" \
"cmdline-tools;latest" \
"platform-tools" && \
success "Installation complete" || \
die "Installation failed" "-2"

# Verify Flutter installation
echo "Check for issues ..."
CHORME_EXECUTABLE=$BROWSER flutter doctor -v
