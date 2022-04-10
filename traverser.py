#!usr/bin/env python3

#Script to visit all folders and run rename.py and duplicate_remover.py in each folder

import os
import subprocess
import sys

script_arg = sys.argv[1]

#function to visit every folder in the path
def traverse(path_to_folder):
