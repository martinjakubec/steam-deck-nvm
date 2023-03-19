from os import path, system
from sys import argv
from list import get_node_versions

def use_node_version():
    if (len(argv) <= 2):
        print("Version argument is also needed.")
        exit()
    version_number = argv[2]
    if (get_node_versions().count(version_number) != 0):
        f = open(path.expanduser("~/node/current_used_version"), "w")
        f.write(version_number)
        print(f"Now using version number {version_number}")
        print("Make sure to source/reload your terminal with 'source ~/.bashrc'")
    else:
        print(f"Version {version_number} not found.")
        exit()