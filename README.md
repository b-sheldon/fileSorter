# fileSorter
A python script to sort files into directories based on their file type

#### Use: python fileSorter.py sortType targetDirectoryName

## Supported sortTypes:
### 1. default
#### Use: python fileSorter.py default path/to/target/directory

The default flag will sort the files provided in the target directory into new directories based on their file type (pdf, txt, py, png, etc.).

### 2. Documents
#### Use: python fileSorter.py Documents TargetDirectory

The Documents flag will sort files based on the file's name. It should only be used to sort directories in the ~/Documents directory. The naming convention for each file is: Category1-Category2-FileName.filetype, where Category1 is the first directory files will be sorted into, Category2 is the second directory files will be sorted into, and FileName will be the new name of the file once it's sorted. 
