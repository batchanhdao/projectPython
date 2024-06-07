from abc import abstractmethod
import os
mô tả nghiệp vụ move file, 
# Path: python/app_python/auto_easy/sap-xep-files.py
ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
NUMBER = '0123456789'
class Folder:
    def __init__(self, path):
        self.path = os.path.normpath(path)
        self.files = []
        self.folders = []
        self.get_files()
        self.get_folders()

    def get_files(self):
        for file in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, file)):
                self.files.append(file)

    def get_folders(self):
        for folder in os.listdir(self.path):
            if os.path.isdir(os.path.join(self.path, folder)):
                self.folders.append(folder)

    def show_files(self):
        print("Files in folder:")
        for file in self.files:
            print(file)

    def show_folders(self):
        print("Folders in folder:")
        for folder in self.folders:
            print(folder)

class FileRename():

    # def __init__(self, path):
    #     super().__init__(path)
    def rename_files(self, folder_path, name_old, name_new):
        os.rename(os.path.join(folder_path, name_old), os.path.join(folder_path, name_new))

class FolderRename():

    # def __init__(self, path):
    #     super().__init__(path)
    def rename_folders(self, folder_path, name_old, name_new):
        os.rename(os.path.join(folder_path, name_old), os.path.join(folder_path, name_new))

# nhóm file theo đuôi: 
class GroupFileByExtension(Folder):
    def __init__(self, path):
        super().__init__(path)
        self.group_files()

    def group_files(self):
        for file in self.files:
            name, extension = os.path.splitext(file)
            extension = str(extension).strip()
            if not os.path.exists(os.path.join(self.path, extension)):
                os.mkdir(os.path.join(self.path, extension))
            try:
                if os.path.exists(os.path.join(self.path, extension, file)):
                    os.remove(os.path.join(self.path, extension, file))
                os.rename(os.path.join(self.path, file), os.path.join(self.path, extension, file))
            except:
                print(f'Error: {file}')

# nhóm file theo ky tu dau tien: tạo thư mục theo ky tu dau tien và di chuyen file vào thư mục đó
class GroupFileByFirstLetter(Folder):
    def __init__(self, path):
        super().__init__(path)
        self.group_files()

    def group_files(self):
        for file in self.files:
            name, extension = os.path.splitext(file)
            first_letter = name[0]
            if not os.path.exists(os.path.join(self.path, first_letter)):
                os.mkdir(os.path.join(self.path, first_letter))

            try:
                if os.path.exists(os.path.join(self.path, first_letter, file)):
                    os.remove(os.path.join(self.path, first_letter, file))
                os.rename(os.path.join(self.path, file), os.path.join(self.path, first_letter, file))
            except:
                print(f'Error: {file}')
            
# nhóm file theo ngay download: tạo thư mục theo ngay download và di chuyen file vào thư mục đó
from datetime import datetime
class GroupFileByDateDownload(Folder):
    def __init__(self, path):
        super().__init__(path)
        self.group_files()

    def group_files(self):
        for file in self.files:
            name, extension = os.path.splitext(file)
            date = os.path.getctime(os.path.join(self.path, file))
            date = datetime.fromtimestamp(date)
            date = str(date).split(' ')[0]
            if not os.path.exists(os.path.join(self.path, date)):
                os.mkdir(os.path.join(self.path, date))
            try:
                if os.path.exists(os.path.join(self.path, date, file)):
                    os.remove(os.path.join(self.path, date, file))
                os.rename(os.path.join(self.path, file), os.path.join(self.path, date, file))
            except:
                print(f'Error: {file}')
    
# di chuyen file theo duoi: tạo thư mục theo duôi và di chuyen file vào thư mục đó    
class MoveFileByExtension(Folder):
    def __init__(self, path):
        super().__init__(path)

    def move_files(self, move_path):
        for file in self.files:
            name, extension = os.path.splitext(file)
            extension = str(extension).strip()
            if not os.path.exists(os.path.join(move_path, extension)):
                os.mkdir(os.path.join(move_path, extension))
            if os.path.exists(os.path.join(move_path, extension, file)):
                os.remove(os.path.join(move_path, extension, file))
            os.rename(os.path.join(self.path, file), os.path.join(move_path, extension, file))

class NameFile():
    def __init__(self, name: str, extension: str) -> None:
        self.name = name
        self.extension = extension

    def __str__(self) -> str:
        return f'name: {self.name} - extension: {self.extension}'
    
class CutNameFile(NameFile):
    # start: 1, lấy từ vị trí bat_dau
    def cut_name(self, bat_dau: int, ket_thuc: int) -> str:
        name = self.name
        if bat_dau > ket_thuc:
            bat_dau = 1
            ket_thuc = len(name)
        if bat_dau <= 0:
            bat_dau = 1
        if ket_thuc >= len(name):
            ket_thuc = len(name)
        name = name[bat_dau-1: ket_thuc]
        return name.strip()
    
class AddNameFile(NameFile):

    def add_on_before_name(self, text) -> str:
        name = self.name
        name = text + name
        return name

    def add_on_after_name(self, text) -> str:
        name = self.name
        name = name + text
        return name
    
    def add_on_name(self, text, place: int) -> str:
        name = self.name
        if place <= 1:
            name = self.add_on_before_name(text=text)
        elif place > len(name):
            name = self.add_on_after_name(text=text)
        else:
            name = name[0:place-1] + text + name[place-1:]

        return name

    


path = 'D:/test'

group = GroupFileByExtension(path)
group.group_files()
folder_cha = Folder(path)
folders_con = folder_cha.folders
i=1
for folder in folders_con:
    folder_con_path = os.path.join(folder_cha.path, folder)
    for file in os.listdir(folder_con_path):
        old_name = file
        name, extension = os.path.splitext(file)
        # extension = str(extension).strip()

        cut_name = CutNameFile(name=name, extension=extension)
        name = cut_name.cut_name(6,60)

        text =f"{i}"

        while len(text) < 4:
            text = '0' + text 
        text = f'I{text}_'

        add_name = AddNameFile(name=name, extension=extension)
        name = add_name.add_on_before_name(text=text)

        new_name = f"{name}{extension}"
        print(new_name)
        rename_file = FileRename()
        # rename_file.rename_files_in_folders_con(folder_con_path, old_name, new_name)
        # os.rename(os.path.join(folder_con_path, file), os.path.join(folder_con_path, new_name))
        i+=1

# folder.show_files()
# folder.show_folders()

