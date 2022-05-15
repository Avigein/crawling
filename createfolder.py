import os

folderList = "html css javascript python java c++".split()

print(folderList)

def createFolder(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print("Error: Creating path. " + path)

for currentFolder in folderList:
    path = "folder_path/" + str(currentFolder)
    createFolder(path)