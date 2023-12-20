import os
import sys

if len(sys.argv) != 3:
    print("Incorrect Arguments Provided, use: python fileSorter.py sortType targetDirectory")
    exit()
    
if (sys.argv[1] != "default" and sys.argv[1] != 'Documents'):
    print("Invalid Arguments Provided, use: python fileSorter.py sortType targetDirectory")
    exit()

if sys.argv[1] == "default":
    # Validate given argument is an existing directory
    target = sys.argv[2]
    if not os.path.isdir(target):
        print("Invalid Directory Provided, use: python fileSorter.py sortType targetDirectory")
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

# When using Documents sorting, the files should be named as follows: Category 1-Category 2-File Name.filetype
elif sys.argv[1] == 'Documents':
    target = os.path.expanduser('~') + '/Documents/' + sys.argv[2]
    if not os.path.isdir(target):
        print("Provided directory does not exist in ~/Documents")
        exit()

    directories = { }
    # Create a list of all directories in the target directory
    for directory in os.listdir(target):
        if not os.path.isfile(directory):
            directories[directory] = directory

    # Loop through all files in the target directory
    for file in os.listdir(target):
        if os.path.isfile(target + '/' + file):
            # Check to see if directory already exists of this file type
            split = file.split('-')

            # Ignore files using the incorrect format
            if len(split) < 3:
                continue

            property = split[0]

            # Create a new directory for Category1 if it doesn't exist, add it to known directories
            if property not in directories:
                os.mkdir(target + '/' + property)
                directories[property] = property
            type = split[1]

            # Create a new directory for Category2 if it doesn't exist, add it to known directories
            if property + '/' + type not in directories:
                os.mkdir(target + '/' + property + '/' + type)
                directories[property + '/' + type] = property + '/' + type

            # Move the file to the correct directory
            os.rename(target + '/' + file, target + '/' + property + '/' + type + '/' + split[2])
        