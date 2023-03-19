from sys import argv
from os import path, remove
from list import get_node_versions
from urllib import request, error
from consts import github_repo_link
import tarfile

temp_file_name = "temp.tar.gz"

def install_node_version():
    if (len(argv) <= 2):
        print("Version argument is also needed.")
        exit()
    version_number = argv[2]
    if (get_node_versions().count(version_number) != 0):
        print(f"Version {version_number} already installed. Use nvm -u {version_number} to use it.")
        exit()
    else:
        print(f"Should install version {version_number}")
        try:
            (path_to_file, data) = request.urlretrieve(
                f"https://nodejs.org/download/release/v{version_number}/node-v{version_number}-linux-x64.tar.gz", temp_file_name
            )
        except error.HTTPError as err: 
            if ("404" in str(err)):
                print(f"Version {version_number} does not exist. Exiting.")
            else:
                print(f"HTTP call failed. Error: {str(err)}")
            exit()
        except:
            print(f"An error occured, try again. If it doesn't work, make sure to raise an issue on github: {github_repo_link}")
            exit()

        tar = tarfile.open(temp_file_name)
        tar.extractall(path.expanduser("~/node/"))
        tar.close()
        remove(temp_file_name)

        print(f"Node {version_number} successfully installed. Use nvm -u {version_number} to use it.")
        exit()