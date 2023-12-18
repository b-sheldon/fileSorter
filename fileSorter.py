import os
import sys

if len(sys.argv) != 2:
    print("Incorrect Arguments Provided, use: python fileSorter.py targetDirectory")
    exit()

# Validate given argument is an existing directory
target = sys.argv[1]
if not os.path.isdir(target):
    print("Invalid Directory Provided, use: python fileSorter.py targetDirectory")
    exit()
    

directories = { }
# Create a list of all directories in the target directory
for directory in os.listdir(target):
    if not os.path.isfile(directory):
        directories[directory] = directory

# Loop through all files in the target directory
for file in os.listdir(target):
    if os.path.isfile(target + '/' + file):
        # check to see if directory already exists of this file type
        split = file.split( '.' )
        newDirectory = split[ 1 ] + ' Files'

        # Create a new directory for this file type if it doesn't exist
        if newDirectory not in directories:
            os.mkdir(target + '/' + newDirectory)
        # Otherwise, add this directory to the known directories Dictionary
        else:
            directories[newDirectory] = newDirectory

        # Move the file to the file type directory
        os.rename(target + '/' + file, target + '/' + newDirectory + '/' + file)
        