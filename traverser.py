#!usr/bin/env python3
#Script to visit all folders and run rename.py and duplicate_remover.py in each folder

import os
import subprocess
import sys

script_arg = sys.argv[1]

def list_all_subdirectories(script_arg):
    """
    Lists all subdirectories in a folder
    """
    for root, dirs, files in os.walk(script_arg):
        for d in dirs:
            print(os.path.join(root, d))

#function run rename.py and duplicate_remover.py for each directory returned by list_all_subdirectories
def traverse(script_arg):
    """
    Runs rename.py and duplicate_remover.py for each directory returned by list_all_subdirectories
    """
    for root, dirs, files in os.walk(script_arg):
        for d in dirs:
            subprocess.call(["python3", "file_manipulation/rename.py", os.path.join(root, d)])
            subprocess.call(["python3", "file_manipulation/duplicate_remover.py", os.path.join(root, d)])
