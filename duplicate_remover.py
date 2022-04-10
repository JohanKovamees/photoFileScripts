#!usr/bin/env python3
#Script that compares all .jpg & .png in a folder and removes duplicate files

#Suggestion for improvement: Base delete on numpy objects that are equal instead of comparing the filesize

import os
#import numpy as np

path_to_folder = input("Enter the path to the folder: ")

def duplicate_remover(path_to_folder):
    """
    Compares all .jpg & .png in a folder and removes duplicate files
    """
    for filename in os.listdir(path_to_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            if os.path.getsize(os.path.join(path_to_folder, filename)) in os.listdir(path_to_folder):
                os.remove(os.path.join(path_to_folder, filename))