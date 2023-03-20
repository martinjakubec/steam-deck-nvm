from os import path, getcwd
from sys import argv

nvm_start_comment = "# nvm start"
nvm_end_comment = "# nvm end"

setup_to_append = f"""
{nvm_start_comment}
NODE_VERSION=$(<~/node/current_used_version)

export PATH="$HOME/node/node-v${{NODE_VERSION}}-linux-x64/bin:$PATH"

alias nvm="python {getcwd()}/nvm.py"
{nvm_end_comment}"""

# remove old setup
file = open(path.expanduser("~/.bashrc"), "r")
file_str = file.read()
file.close()
if (nvm_start_comment in file_str and nvm_end_comment in file_str):
  stitch_1 = file_str[0:(file_str.index(nvm_start_comment)-1)]
  stitch_2 = file_str[file_str.index(nvm_end_comment) + len(nvm_end_comment) + 1:]

  file = open(path.expanduser("~/.bashrc"), "w")
  file.write(stitch_1 + stitch_2)
  file.close()

if (len(argv) > 1 and argv[1] == 'remove'):
  exit()

# append new setup
file = open(path.expanduser("~/.bashrc"), "r")
file_str = file.read()
file.close()
file_str += setup_to_append

file = open(path.expanduser("~/.bashrc"), "w")
file.write(file_str)
file.close()

print("Setup complete, reopen your terminal or source it using 'source ~/.bashrc'")