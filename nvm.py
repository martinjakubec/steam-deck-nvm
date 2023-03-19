from sys import argv
from list import list_node_versions
from use import use_node_version
from install import install_node_version

def main():
    if (len(argv) > 1):
        match argv[1]:
            case ('list' | '-l'):
                list_node_versions()   
            case ('use' | '-u'):
                use_node_version()
            case ('install' | 'i'):
                install_node_version()
            case ('remove' | '-r'):
                print('should remove a version')
            case _:
                print('should show help with command not found')
    else:
        print('should show default help')

main()