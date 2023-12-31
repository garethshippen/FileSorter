# Garet Shippen
# December 2023
# Sorts files in the directory the script is in, into subdirectories
# based on the file's extension.

import os, shutil

this_file = os.path.basename(__file__)
base = os.getcwd()

# Split directory contents into directorys and files
def filter(path):
    dirs = []
    files = []
    for item in os.listdir(path):
        if item == this_file:
            continue
        if os.path.isfile(os.path.join(path, item)):
            files.append(item)
        else:
            dirs.append(item)
    return dirs, files
dirs, files = filter(base)

# Create any missing directories
extensions = list(set([file.split(".")[-1].lower() for file in files]))
for extension in extensions:
    if extension not in dirs:
        new_dir = os.path.join(base, extension)
        os.mkdir(new_dir)
        #print("Made directory '{}'".format(extension))

# Move files into directories based on their extension
for file in files:
    if file == this_file: # Leave this script in the base directory
        continue
    target_dir = file.split(".")[-1]
    new_path = os.path.join(base, target_dir, file)
    shutil.move(file, new_path)
