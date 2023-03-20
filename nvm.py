from sys import argv
from list import list_node_versions
from use import use_node_version
from install import install_node_version
from remove import remove_node_version
from help import show_help
from available import show_available_versions

def main():
    if (len(argv) > 1):
        match argv[1]:
            case ('list' | '-l'):
                list_node_versions()   
            case ('use' | '-u'):
                use_node_version()
            case ('install' | '-i'):
                install_node_version()
            case ('remove' | '-r'):
                remove_node_version()
            case ('help' | '-h'):
                show_help()
            case ('available' | '-a'):
                show_available_versions()
            case _:
                print(f"Command '{argv[1]}' not found. Use nvm help or nvm -h to show help.")
    else:
        show_help()

main()
