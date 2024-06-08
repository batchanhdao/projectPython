from abc import abstractmethod
import os
# Path: python/app_python/auto_easy/sap-xep-files.py
# update file in folder cha/con/both
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

    # def __init__(self, path):
    #     super().__init__(path)

    # add text to name file, create new name, danh so auto, cut name
    def create_new_name(self, name_new, vi_tri_add_text: int = 1, number_start=1, len_number=4):
        for file in self.files:
            if os.path.isdir(os.path.join(self.path, file)):
                continue
            name_old = file
            name, extension = os.path.splitext(file)
            text = Text().create_number(number_start=number_start, len_number=len_number)
            number_start+=1
            add_name = AddNameFile(name=name_new, extension=extension)
            name_new = add_name.add_on_name(text=text, place=vi_tri_add_text)
            name_new = f"{name_new}{extension}"
            return self.rename(self.path, name_old, name_new)
    
    def add_text_to_name(self, text, vi_tri_add_text: int = 1):
        for file in self.files:
            if os.path.isdir(os.path.join(self.path, file)):
                continue
            name_old = file
            name, extension = os.path.splitext(file)
            add_name = AddNameFile(name=name, extension=extension)
            name_new = add_name.add_on_name(text=text, place=vi_tri_add_text)
            name_new = f"{name_new}{extension}"
            return self.rename(self.path, name_old, name_new)
        
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
            return self.rename(self.path, name_old, name_new)
    
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
            return self.rename(self.path, name_old, name_new)


    def edit_files_in_folders_con(self, vi_tri_cut_name = {'bat_dau': None, 'ket_thuc': None}, vi_tri_add_text: int = 1, number_start=1, len_number=4):
        alpha_id = 0
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
                text = Text().create_char_and_number(char=ALPHA[alpha_id], number_start=number, len_number=len_number)
                add_name = AddNameFile(name=name, extension=extension)
                name_new = add_name.add_on_name(text=text, place=vi_tri_add_text)
                number+=1
                name_new = f"{name_new}{extension}"
                print(self.rename(folder_path, name_old, name_new))
            alpha_id+=1


    def rename(self, folder_path, name_old, name_new):
        try:
            # os.rename(os.path.join(folder_path, name_old), os.path.join(folder_path, name_new))
            print(f"Success rename file: {name_old} to {name_new}")
            return True
        except Exception as e:
            print(e)
            return False

class FolderUpdate(Folder):
    def __init__(self, path):
        super().__init__(path)

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

    def create_char_and_number(self, char: str, number_start=1, len_number=4):
        text = str(number_start)
        while(len(text) < len_number):
            text = '0' + text
        text = f'{char}{text}_'
        return text
    
    def create_number(self, number_start=1, len_number=4):
        text = str(number_start)
        while(len(text) < len_number):
            text = '0' + text
        text = f'{text}_'
        return text
        

path = 'D:/test'

# group = GroupFileByExtension(path)
# group.group_files()
folder_cha = Folder(path)
folders_con = folder_cha.folders

# folder.show_files()
# folder.show_folders()

class SelectAction():
    def __init__(self) -> None:
        pass

    def select_action(self):
        print("Select action:")
        print("1. Group file by extension")
        print("2. Group file by first letter")
        print("3. Group file by date download")
        print("4. Move file by extension")
        print("5. Rename files")
        print("6. Edit files in folder")
        print("7. Edit files in folders con")
        print("8. Exit")
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
    
class Input():
    def __init__(self) -> None:
        pass

    def get_input(self, messenge) -> str:
        text = input('NHAP "ex" TO END or ' + messenge).strip()
        if text == 'ex':
            exit()
        return text
    
class InputCut():
    def get_input(self) -> dict:
        result = {"bat_dau": None, "ket_thuc": None}
        text = input('Nhap "no" To Pass or Cut "start, end": ').strip()
        if text == 'no':
            return result
        text = text.split(',')
        if len(text) != 2:
            return result
        if not text[0].isdigit() or not text[1].isdigit():
            return result
        result['bat_dau'] = int(text[0])
        result['ket_thuc'] = int(text[1])
        return result

class InputAdd():
    def get_input(self) -> int:
        text = input('Add "vi tri": ').strip()
        if not text.isdigit():
            return 1
        return int(text)

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
    nhap = Input()

    while True:
        input_cut = InputCut()
        input_add = InputAdd()
        action = main.get_action()
        print(main.action)
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
            move = MoveFileByExtension(path)
            move.move_files('D:/test1')
        elif action == '5':
            file = FileRename(path)
            name_new = nhap.get_input('Enter name new: ')
            vi_tri_add_text = input_add.get_input()
            file.rename_files(name_new, vi_tri_add_text=vi_tri_add_text)
        elif action == '6':
            file = FileRename(path)
            vi_tri_cut_name = input_cut.get_input()
            vi_tri_add_text = input_add.get_input()
            file.edit_files_in_folder_cha(vi_tri_cut_name=vi_tri_cut_name, vi_tri_add_text=vi_tri_add_text)
        elif action == '7':
            file = FileRename(path)
            vi_tri_cut_name = input_cut.get_input()
            vi_tri_add_text = input_add.get_input()
            file.edit_files_in_folders_con(vi_tri_cut_name=vi_tri_cut_name, vi_tri_add_text=vi_tri_add_text)
        elif action == '8':
            print("Exit")
            break
        else:
            print("Action not found")
            print("Please select action again")
