#Script to rename all .png & .jpg files in a folder to numerical values
# 

#!/usr/bin/env python3

import os

path_to_folder = input("Enter the path to the folder: ")

def renamer(path_to_folder):
    """
    Renames all files in a folder to numerical values
    """
    for filename in os.listdir(path_to_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            os.rename(os.path.join(path_to_folder, filename), os.path.join(path_to_folder, str(os.path.getsize(os.path.join(path_to_folder, filename))) + ".jpg"))