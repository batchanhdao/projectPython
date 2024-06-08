import os
import shutil
from input_type import InputText, InputCut, InputAdd, InputAutoNumber
from group_type import GroupFileByExtension, GroupFileByFirstLetter, GroupFileByDateDownload
from change_file import FileRename
from move_file import MoveFileByExtension

class SelectAction():
    def __init__(self) -> None:
        pass

    def select_action(self):
        print("Select action:")
        print("1. Group file by extension")
        print("2. Group file by first letter")
        print("3. Group file by date download")
        print("4. Create new name in files")
        print("5. Cut name in files")
        print("6. Add text in files")
        print("7. Auto number in files")
        print("8. Edit files in folders con")
        print("0. Exit")
        action = input("Select action: ").strip()
        return action
    
class Path():
    def __init__(self) -> None:
        pass

    def get_path(self) -> str:
        path = ''
        while True:
            try:
                path = input("Enter path: ").strip()
                path = os.path.normpath(path)
                check_path = os.path.exists(path)
                if not check_path:
                    print("Path not found")
                    print("Please enter path again")
                else:
                    break
            except Exception as e:
                print("Error Path Format:", e)
                print("Please enter path again")
        return path

class Main():
    def __init__(self) -> None:
        pass

    def get_path(self):
        path = Path()
        return path.get_path()

    def get_action(self):
        select_action = SelectAction()
        return select_action.select_action()

if __name__ == '__main__':
    main = Main()
    path = main.get_path()

    while True:
        nhap = InputText()
        input_cut = InputCut()
        input_add = InputAdd()
        input_auto_number = InputAutoNumber()
        action = main.get_action()
        print("action: ", action)
        if action == '1':
            group = GroupFileByExtension(path)
            group.group_files()
        elif action == '2':
            group = GroupFileByFirstLetter(path)
            group.group_files()
        elif action == '3':
            group = GroupFileByDateDownload(path)
            group.group_files()

        elif action == '4':
            file = FileRename(path)
            new_name = nhap.get_input('Enter name new: ')
            number = input_auto_number.get_input()
            vi_tri_add_text = input_add.get_input()
            file.create_new_name(new_name=new_name, vi_tri_add_text=vi_tri_add_text, number_start=number['number_start'], len_number=number['len_number'])
        elif action == '5':
            file = FileRename(path)
            vi_tri_cut_name = input_cut.get_input()
            file.cut_name_in_file(vi_tri_cut_name=vi_tri_cut_name)
        elif action == '6':
            file = FileRename(path)
            text = nhap.get_input('Enter text: ')
            vi_tri_add_text = input_add.get_input()
            file.add_text_to_name(text=text, vi_tri_add_text=vi_tri_add_text)
        elif action == '7':
            file = FileRename(path)
            number = input_auto_number.get_input()
            vi_tri_add_text = input_add.get_input()
            file.auto_number(vi_tri_add_text=vi_tri_add_text, number_start=number['number_start'], len_number=number['len_number'])
        elif action == '8':
            file = FileRename(path)
            vi_tri_cut_name = input_cut.get_input()
            number = input_auto_number.get_input()
            vi_tri_add_text = input_add.get_input()
            file.edit_files_in_folders_con(vi_tri_cut_name=vi_tri_cut_name, vi_tri_add_text=vi_tri_add_text, number_start=number['number_start'], len_number=number['len_number'])
        
        elif action == '0':
            print("Exit")
            break
        else:
            print("Action not found")
            print("Please select action again")


# from change_file import ChangeFile


# CHANGE_FILE = ChangeFile()
# CHANGE_FILE
# LIST_FORDEL = {}

# def CreateFolders(path):
#     try:
#         files = os.listdir(path)
#         print(files)
#         for file in files:
#             if os.path.isdir(os.path.join(path, file)):
#                 continue
#             else:
#                 name, extension = os.path.splitext(file)
#                 extension = extension[1:]
#                 path_folder = os.path.join(path, extension)
#                 path_file = os.path.join(path, file) 
#                 if os.path.exists(path_folder):
#                     shutil.move(path_file, os.path.join(path_folder, file))
#                 else:
#                     os.makedirs(path_folder)
#                     shutil.move(path_file, os.path.join(path_folder, file))
#         print("---------Finished!---------")
#     except Exception as e:
#         print(e)

# def ListFolders(path):
#     global LIST_FORDEL
#     LIST_FORDEL.clear()
#     print("---------List Folder------------")
#     try:
#         i=1
#         for d in os.listdir(path): 
#             link = os.path.join(path, d)
#             if os.path.isdir(link):
#                 LIST_FORDEL[str(i)]=link
#                 print(str(i) + ": " + d)
#                 i+=1
    
#     except Exception as e:
#         print(e)

# def GroupFolder(name, key_folder):
#     global LIST_FORDEL
#     folder_source = LIST_FORDEL[key_folder]
#     try:
#         if os.path.exists(name):
#             if os.path.exists(os.path.join(name, os.path.split(folder_source)[1])):
#                 for f in os.listdir(folder_source):
#                     try:
#                         source = os.path.join(folder_source, f)
#                         to = os.path.join(name, os.path.split(folder_source)[1])
#                         shutil.move(source, to)
#                     except Exception as e:
#                         print(e)
#                 shutil.rmtree(folder_source)
#             else:
#                 shutil.move(folder_source, name)
#         else:
#             os.makedirs(name)
#             shutil.move(folder_source, name)
    
#     except Exception as e:
#         print(e)

# def main(path):
#     try:
#         while(True):
#             key = input("""Options:
#     'ok' to auto-create files 
#     '1' to group folders
#     '2' to change extension
#     'ex' to exit
#     Enter your choice: """).strip()
#             if key == 'ok':
#                 CreateFolders(path)
#             elif key == "1":
#                 ListFolders(path)
#                 name = input("Name's folder: ").strip()
#                 key_folders = input("Number's folder1 + , + ...: ").strip().split(",")
#                 name = os.path.join(path, name)
#                 os.path.normpath(name)
#                 for k in key_folders:
#                     k = k.strip()
#                     GroupFolder(name, k)
#                 print("-----------Finished!----------")
#             elif key == "2":
#                 CHANGE_FILE.Extension(path)

#             elif key == "ex":
#                 return
#             else:
#                 print("-------Unknow--------")
        
#     except Exception as e:
#         print(e)

# while(True):
#     path = input("ENTER PATH or '0' to END: ").strip()
#     if path == '0':
#         break
#     else:
#         os.path.normpath(path)
#         # path = 'C:\\Users\\Admin\\Pictures\\Screenshots'
#         main(path)