import os
import shutil
from change_file import ChangeFile


CHANGE_FILE = ChangeFile()
CHANGE_FILE
LIST_FORDEL = {}

def CreateFolders(path):
    try:
        files = os.listdir(path)
        print(files)
        for file in files:
            if os.path.isdir(os.path.join(path, file)):
                continue
            else:
                name, extension = os.path.splitext(file)
                extension = extension[1:]
                path_folder = os.path.join(path, extension)
                path_file = os.path.join(path, file) 
                if os.path.exists(path_folder):
                    shutil.move(path_file, os.path.join(path_folder, file))
                else:
                    os.makedirs(path_folder)
                    shutil.move(path_file, os.path.join(path_folder, file))
        print("---------Finished!---------")
    except Exception as e:
        print(e)

def ListFolders(path):
    global LIST_FORDEL
    LIST_FORDEL.clear()
    print("---------List Folder------------")
    try:
        i=1
        for d in os.listdir(path): 
            link = os.path.join(path, d)
            if os.path.isdir(link):
                LIST_FORDEL[str(i)]=link
                print(str(i) + ": " + d)
                i+=1
    
    except Exception as e:
        print(e)

def GroupFolder(name, key_folder):
    global LIST_FORDEL
    folder_source = LIST_FORDEL[key_folder]
    try:
        if os.path.exists(name):
            if os.path.exists(os.path.join(name, os.path.split(folder_source)[1])):
                for f in os.listdir(folder_source):
                    try:
                        source = os.path.join(folder_source, f)
                        to = os.path.join(name, os.path.split(folder_source)[1])
                        shutil.move(source, to)
                    except Exception as e:
                        print(e)
                shutil.rmtree(folder_source)
            else:
                shutil.move(folder_source, name)
        else:
            os.makedirs(name)
            shutil.move(folder_source, name)
    
    except Exception as e:
        print(e)

def main(path):
    try:
        while(True):
            key = input("""Options:
    'ok' to auto-create files 
    '1' to group folders
    '2' to change extension
    'ex' to exit
    Enter your choice: """).strip()
            if key == 'ok':
                CreateFolders(path)
            elif key == "1":
                ListFolders(path)
                name = input("Name's folder: ").strip()
                key_folders = input("Number's folder1 + , + ...: ").strip().split(",")
                name = os.path.join(path, name)
                os.path.normpath(name)
                for k in key_folders:
                    k = k.strip()
                    GroupFolder(name, k)
                print("-----------Finished!----------")
            elif key == "2":
                CHANGE_FILE.Extension(path)

            elif key == "ex":
                return
            else:
                print("-------Unknow--------")
        
    except Exception as e:
        print(e)

while(True):
    path = input("ENTER PATH or '0' to END: ").strip()
    if path == '0':
        break
    else:
        os.path.normpath(path)
        # path = 'C:\\Users\\Admin\\Pictures\\Screenshots'
        main(path)