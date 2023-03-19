from sys import argv
from shutil import rmtree
from list import get_node_versions
from os import path
from consts import github_repo_link

def remove_node_version():
    if (len(argv) <= 2):
        print("Version argument is also needed.")
        exit()  
    version_number = argv[2]
    if (get_node_versions().count(version_number) != 0):
        try:
            rmtree(path.expanduser(f"~/node/node-v{version_number}-linux-x64"))
            print(f"Version {version_number} successfully removed.")
        except OSError as err:
            if (err.errno == 2):
                print(f"Version {version_number} not found even if it seems to exist. Please raise an issue on github: {github_repo_link}")
                exit()
            else:
                print(f'Could not remove version. Please raise an issue on github: {github_repo_link}')
                exit()
                
    else:
        print(f"Version {version_number} not found.")
        exit()