from sys import argv
from shutil import rmtree
from list import get_node_versions
from urllib import request, error
import json
from os import path
from consts import github_repo_link

def remove_node_version():
    if (len(argv) <= 2):
        print("Version argument is also needed.")
        exit()  
    version_number = argv[2]
    if version_number == 'latest':
        url = request.urlopen(f"https://nodejs.org/download/release/index.json")
        data = json.load(url)
        version_number = data[0]['version'][1:]
    if version_number == 'lts':
        url = request.urlopen(f"https://nodejs.org/download/release/index.json")
        data = json.load(url)
        filtered_version = filter(lambda version: version['lts'] != False, data)
        version_number = next(filtered_version)['version'][1:]
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