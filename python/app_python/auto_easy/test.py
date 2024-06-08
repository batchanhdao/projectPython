import os
import shutil

# path = input("ENTER PATH: ")
# os.path.normpath(path)
# i=1
# LIST_FORDEL = {}
# for d in os.listdir(path): 
#     link = os.path.join(path, d)
#     if os.path.isdir(link):
#         LIST_FORDEL[str(i)]=link
#         print(str(i) + ": " + d)
#         i+=1
# print(LIST_FORDEL.get("1"))
# print(os.path.split(LIST_FORDEL.get("1"))[1])

# dic = {"1": 1, "2": 2}
# print(dic)

a = 'anh'
a = a
print(a[0:2])

class NameFile():
    def __init__(self, name: str, extension: str) -> None:
        self.name = name
        self.extension = extension

    def __str__(self) -> str:
        return f'name: {self.name} - extension: {self.extension}'
    
class CutNameFile(NameFile):
    # start: 1
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
        return name

cut = CutNameFile('anh', 'txt')
name = cut.cut_name(1, 4)
print(name)

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

add = AddNameFile('anh', 't')
b = add.add_on_before_name('gdt')
a = add.add_on_after_name('gdt')
n = add.add_on_name("gdt", 4)
print(b,a,n)

t = '.anh'
print(t.strip(''))

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
            print(date)
            date = str(date).split(' ')[0]
            print(date)

# path = 'D:/test'

# group = GroupFileByDateDownload(path)
# group.group_files()

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

# path = 'D:/test'

# move = MoveFileByExtension(path)
# move.move_files('D:/test1')

class Text():
    def __init__(self) -> None:
        pass

    def char_and_number_auto_tang(self, char: str, number_start=1, len_number=4):
        text = str(number_start)
        while(len(text) < len_number):
            text = '0' + text
        text = f'{char}{text}_'
        return text
    
    def number_auto_tang(self, number_start=1, len_number=4):
        text = str(number_start)
        while(len(text) < len_number):
            text = '0' + text
        text = f'{text}_'
        return text
    
# t = Text()
# print(t.char_and_number_auto_tang('a', 4, 6))
# print(t.number_auto_tang(1, 4))

a = '0001_'
if a.isdigit():
    print('ok')
else:
    print('no')