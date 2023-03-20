import json
from urllib import request
from list import get_node_versions

def show_available_versions():
    url = request.urlopen(f"https://nodejs.org/download/release/index.json")
    data = json.load(url)
    data = data[::-1]
    for version in data:
        installed = " (installed)" if get_node_versions().count(version['version'][1:]) != 0 else ""
        print(version['version'][1:] + installed)
