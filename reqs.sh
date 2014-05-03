#!/usr/bin/env zsh

if [[ -z "$VIRTUAL_ENV" ]] ; then
    echo "Please run in a virtual environment"
    exit 1
fi

# install system packages
sudo apt-get install bison libportaudio2 libportaudio19-dev gfortran
pip install pyaudio

# get homebrew
BREW="$VIRTUAL_ENV/linuxbrew"
git clone "https://github.com/justjake/linuxbrew" "$VIRTUAL_ENV/linuxbrew"
add-bundle-to-path "$VIRTUAL_ENV/linuxbrew"

# install brew packages
cd "$BREW"
git checkout add-phonetisaurus

brew install openfst --with-fsts-options
brew install MITLM m2m-aligner
brew install cmu-pocketsphinx cmuclmtk phonetisaurus
