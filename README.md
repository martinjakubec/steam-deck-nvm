# NVM for Steam Deck

NVM substitute for Steam Deck with readonly system.

## Why even do this when NVM exists already?

Since I didn't want to mess with readonly system on SD and installing the original nvm, I decided to create my own one written in python. I have chosen python because it is already installed on SD and accessible via konsole.

## How does it work?

It puts this config into your .bashrc file:

```bash
NODE_VERSION=$(<~/node/current_used_version)

export PATH="$HOME/node/node-v${NODE_VERSION}-linux-x64/bin:$PATH"

alias nvm="python {getcwd()}/nvm.py"
```

1. It creates a file which stores your current used version
1. Whenever you then open a konsole, it reads current version and adds it to your path, so now your node and npm binaries can be used from command line
1. It adds an alias to the nvm script, allowing you to use it from anywhere

**Note:** This config is surrounded by comments so that it can be later removed. For removal, see [this section](#removal)

## Installation

Download the release, extract it into a folder where you want this tool to be located, run `python setup.py` and close/open your terminal (or source it using `source ~/.bashrc` command).

## Usage

This utility comes with the basic nvm functionality, such as installing and switching node versions.

### **list (-l)**

`nvm list` lists all versions that are available on your system. These are pulled out of `~/node` directory where this nvm downloads node version. If you decide to download versions manually, you can do so and by putting them in this folder, nvm will check them when installing/switching versions. You need to retain the official package name.

### **install (-i)**

`nvm install <version>` installs the version you specify. This version is then installed into `~/node` directory.

You can also use `latest` which will download the latest release, or `lts` which will download latest long term support version.

### **use (-u)**

`nvm use <version>` updates the version that is currently used. Since version is read into your `.bashrc` file, you will need to either reopen your terminal, or source it using `soruce ~/.bashrc` command.

### **remove (-r)**

`nvm remove <version>` removes the version you specify.

You can also use `latest` which will remove the latest release, or `lts` which will remove latest long term support version.

**Note:** Remove always pulls info about latest and lts versions from up-to-date nodejs.org index of versions. This means that installing latest/lts and later wanting to remove them by using `nvm remove latest/lts` might end up in version not being found on your system. In this case, remove the version by using its number.

### **available (-a)**

`nvm available` lists all available versions that can be installed. It also shows which versions are already installed on your system by marking them like this: `vX.Y.Z (installed)`

### **help (-h)**

`nvm help` shows help for all of the commands available in this tool. Help is also shown when running only `nvm` command.

## Removal

If you decide to remove this nvm, you can simply run `python setup.py remove` which will remove any changes made to your `.bashrc` file.

## Issues

If you encounter any problems with this tool, feel free to raise an issue in this github repo.
