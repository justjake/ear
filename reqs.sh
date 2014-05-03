#!/usr/bin/env zsh

if [[ -z "$VIRTUAL_ENV" ]] ; then
    echo "Please run in a virtual environment"
    exit 1
fi

# install system packages
sudo apt-get install bison libportaudio2 libportaudio19-dev gfortran
pip install pyaudio pywit

# get homebrew
BREW="$VIRTUAL_ENV/linuxbrew"
git clone "https://github.com/justjake/linuxbrew" "$VIRTUAL_ENV/linuxbrew"
add-bundle-to-path "$VIRTUAL_ENV/linuxbrew"

# install brew packages
pushd "$BREW"
git checkout add-phonetisaurus
popd

brew install openfst --with-fsts-options
brew install MITLM m2m-aligner
brew install cmu-pocketsphinx cmuclmtk phonetisaurus

# get data
wget http://phonetisaurus.googlecode.com/files/g014b2b.tgz
tar -zxf g014b2b.tgz
pushd g014b2b
./compile-fst.sh
popd

mkdir -p data
mv g014b2b data/
