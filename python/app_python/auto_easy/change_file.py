import os
import fnmatch

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

class FileRename(Folder):

    def __init__(self, path, logger=None):
        super().__init__(path)
        self.logger = logger

    # add text to name file, create new name, danh so auto, cut name
    def create_new_name(self, new_name, vi_tri_add_text: int = 1, number_start=1, len_number=4):
        for file in self.files:
            if os.path.isdir(os.path.join(self.path, file)):
                continue
            name_old = file
            name, extension = os.path.splitext(file)
            text = Text()
            text = text.create_number(number_start=number_start, len_number=len_number)
            number_start+=1
            add_name = AddNameFile(name=new_name, extension=extension)
            name_new = add_name.add_on_name(text=text, place=vi_tri_add_text)
            name_new = f"{name_new}{extension}"
            self.rename(self.path, name_old, name_new)
    
    def add_text_to_name(self, text, vi_tri_add_text: int = 1):
        for file in self.files:
            if os.path.isdir(os.path.join(self.path, file)):
                continue
            name_old = file
            name, extension = os.path.splitext(file)
            add_name = AddNameFile(name=name, extension=extension)
            name_new = add_name.add_on_name(text=text, place=vi_tri_add_text)
            name_new = f"{name_new}{extension}"
            self.rename(self.path, name_old, name_new)
        
    def cut_name_in_file(self, vi_tri_cut_name = {'bat_dau': None, 'ket_thuc': None}): 
        for file in self.files:
            if os.path.isdir(os.path.join(self.path, file)):
                continue
            name_old = file
            name, extension = os.path.splitext(file)
            cut_name = CutNameFile(name=name, extension=extension)
            if vi_tri_cut_name['bat_dau'] and vi_tri_cut_name['ket_thuc']:
                name = cut_name.cut_name(vi_tri_cut_name['bat_dau'], vi_tri_cut_name['ket_thuc'])
            name_new = f"{name}{extension}"
            self.rename(self.path, name_old, name_new)
    
    def auto_number(self, vi_tri_add_text, number_start=1, len_number=4):
        for file in self.files:
            if os.path.isdir(os.path.join(self.path, file)):
                continue
            name_old = file
            name, extension = os.path.splitext(file)
            text = Text().create_number(number_start=number_start, len_number=len_number)
            add_name = AddNameFile(name=name, extension=extension)
            name_new = add_name.add_on_name(text=text, place=vi_tri_add_text)
            number_start+=1
            name_new = f"{name_new}{extension}"
            self.rename(self.path, name_old, name_new)


    def edit_files_in_folders_con(self, vi_tri_cut_name = {'bat_dau': None, 'ket_thuc': None}, vi_tri_add_text: int = 1, number_start=1, len_number=4):
        for folder in self.folders:
            folder_path = os.path.join(self.path, folder)
            number = number_start
            for file in os.listdir(folder_path):
                if os.path.isdir(os.path.join(folder_path, file)):
                    continue
                name_old = file
                name, extension = os.path.splitext(file)
                cut_name = CutNameFile(name=name, extension=extension)
                if vi_tri_cut_name['bat_dau'] and vi_tri_cut_name['ket_thuc']:
                    name = cut_name.cut_name(vi_tri_cut_name['bat_dau'], vi_tri_cut_name['ket_thuc'])
                text = Text().create_char_and_number(number_start=number, len_number=len_number)
                number+=1
                add_name = AddNameFile(name=name, extension=extension)
                name_new = add_name.add_on_name(text=text, place=vi_tri_add_text)
                name_new = f"{name_new}{extension}"
                self.rename(folder_path, name_old, name_new)


    def rename(self, folder_path, name_old, name_new):
        try:
            os.rename(os.path.join(folder_path, name_old), os.path.join(folder_path, name_new))
            self.logger.write(f"Success rename file: '{name_old}' -> '{name_new}'")
            # print(f"Success rename file: '{name_old}' -> '{name_new}'")
            return True
        except Exception as e:
            self.logger.write(f'Error: ', e)
            return False

class FolderRename():

    # def __init__(self, path):
    #     super().__init__(path)
    def rename_folders(self, folder_path, name_old, name_new):
        os.rename(os.path.join(folder_path, name_old), os.path.join(folder_path, name_new))


class NameFile():
    def __init__(self, name: str, extension: str) -> None:
        self.name = name
        self.extension = extension

    def __str__(self) -> str:
        return f'name: {self.name} - extension: {self.extension}'
    
class CutNameFile(NameFile):
    # start: 1, lấy từ >= vị trí bat_dau, <= vị trí ket_thuc
    def cut_name(self, bat_dau: int, ket_thuc: int) -> str:
        name = self.name
        if bat_dau > ket_thuc:
            return name
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

class Text():
    def __init__(self) -> None:
        pass

    def create_char_and_number(self, number_start=1, len_number=4):
        if number_start < 1:
            number_start = 1
        text = str(number_start)
        while(len(text) < len_number):
            text = '0' + text
        text = text + "_"
        return text
    
    def create_number(self, number_start=1, len_number=4):
        if number_start < 1:
            number_start = 1
        text = str(number_start)
        while(len(text) < len_number):
            text = '0' + text
        return text
        



# def ChangeExtension(path, name, old_extension, new_extension):
#     try:
#         os.rename(os.path.join(path, name + old_extension) , os.path.join(path, name + new_extension))
#         print(name + old_extension + " -> " + name + new_extension)
#     except Exception as e:
#         print(e)

# class ChangeFile:
#     def __init__(self):
#         pass

#     def Extension(self, path):
#         extensions = set()
#         try:
#             for f in os.listdir(path):
#                 source = os.path.join(path, f)
#                 name, extension = os.path.splitext(f)
#                 if os.path.isfile(source):
#                     extensions.add(extension)
#         except Exception as e:
#             print(e)
#         print(extensions)

#         # chon oldend va newend
#         old_extension=input("ENTER OLD EXTENSION: ")
#         new_extension=input("ENTER NEW EXTENSION: ")
#         old_extension = '.' + old_extension
#         new_extension = '.' + new_extension
#         try:
#             for f in os.listdir(path):
#                 source = os.path.join(path, f)
#                 name, extension = os.path.splitext(f)
#                 if os.path.isfile(source) and f.endswith(old_extension):
#                     ChangeExtension(path, name, old_extension, new_extension)
#                 else:
#                     continue
#             print("----------Finished----------")
#         except Exception as e:
#             print(e)

        
