'''
    FILE PROCESSING
    - Files = single string value
    - Concepts = 
        a. each files have file name and file path
        b. Root folder = C:\ (Windows) / (Linux and Mac)
        c. The path separator will be \ in windows, and / on mac and linux
        d. File also has extensions -> tells you the type of file
    - In windows, we need to escape the backslash, or use raw string
    - For path, we can use join

    FILE PATHS:
    A. Absolute Path -> start from root
    B. Relative Path -> start from current working directory
'''

import os
# file related functions

# CREATE PATH
path = os.path.join('folder1','folder2', 'folder3','jerry.png')
print(path)

# GET CURRENT LOCATION
print(os.getcwd()) # current working directory

# CHANGE DIRECTORY
# os.chdir("blablabla")

# GET SEPARATOR
print(os.sep)

# GET ABSOLUTE PATH OF A FILE
print(os.path.abspath("0 - Introduction.txt"))

# CHECK IF A FILE PATH IS ABSOLUTE
print(os.path.isabs("0 - Introduction.txt"))

# GIVE THE RELATIVE PATH BETWEEN 2 FILES
print(os.path.relpath("0 - Introduction.txt", "C:\\"))

# GET DIRECTORY PART
print(os.path.dirname(fileName))

# GET BASE PART
print(os.path.basename(fileName))

# CHECK IF PATH EXISTS
print(os.path.exists(fileName))

# GET SIZE
print(os.path.getsize("0 - Introduction.txt"))

# GET FILE INSIDE A FOLDER
filesInFolder = os.listdir(fileName)

# GET SIZE OF EACH FILE IN A FOLDER
totalSize = 0
for i in filesInFolder:
    print(str(os.path.basename(i)) + " : "+ str(os.path.getsize(i)))
    totalSize+= os.path.getsize(i)
print("Total Size: " + str(totalSize))

# READING AND WRITING PLAIN TEXT FILES

# 1. Open function

textfile = open("0 - Introduction.txt") # read mode

# read everything
fileContent = textfile.read()

# close the file
textfile.close()

# must open in write mode or appendmode

writeFile = open("11.5 - FileWritingExample", 'w')
writeFile.write("Hey there, How are you?\n")
writeFile.close()

# append 

appendFile = open("11.5 - FileWritingExample", "a")
appendFile.write("Append Mode")
appendFile.close()

#store nontext data

import shelve 
shelfFile = shelve.open('mydata')
shelfFile['test'] = [1,2,3,4,11]
shelfFile.close()
# creates 3 new files ( .bak, .dir. .dat)

shelfFile = shelve.open('mydata')
print(shelfFile['test'])
shelfFile.close()

# MOVE AND COPY FILES AND FOLDERS

#copy rename remove files using shutil

import shutil
shutil.copy("0 - Introduction.txt", target)

# delete a single file
# os.unlink()

# delete a single folder
# os.rmdir()
# must be empty folder

# delete a folder and all its contents
# shutil.rmtree()

# send a file or folder to a recycling bin
# send2trahs.send2trash()

# WALKING A DIRECTORY TREE
# for folderName, subFolders, fileNames in os.walk('C:\\'):
#     print("The folder is "+ folderName)
#     print("The subfolders are: "+ str(subFolders))
#     print("The filename are: "+ str(fileNames))


