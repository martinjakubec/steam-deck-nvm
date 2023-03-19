from consts import github_repo_link

def show_help():
    print(f"""NVM for Steam Deck help

Usage:

nvm list | -l               Lists all available    
nvm install | -i <version>  Installs the specified version
nvm use | -u <version>      Uses the specified version
nvm remove | -r <version>   Removes the specified version
nvm help | -h               Shows help and usage of NVM for Steam Deck commands

For a more detailed documentation, visit NVM for Steam Deck repo: {github_repo_link}""")