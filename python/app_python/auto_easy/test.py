
import os
import shutil
from change_file import Folder


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
path = Path().get_path()
    
# nhóm file theo đuôi: 
class GroupFileByExtension(Folder):
    def __init__(self, path):
        super().__init__(path)
        self.group_files()

    def group_files(self):
        for file in self.files:
            name, extension = os.path.splitext(file)
            if not os.path.exists(os.path.join(self.path, extension)):
                os.mkdir(os.path.join(self.path, extension))
            try:
                shutil.move(os.path.join(self.path, file), os.path.join(self.path, extension, file))
                # os.rename(os.path.join(self.path, file), os.path.join(self.path, extension, file))
            except Exception as e:
                print(f'Error: {file}', e)

# group = GroupFileByExtension(path)
# group.group_files()

# nhóm file theo ky tu dau tien: tạo thư mục theo ky tu dau tien và di chuyen file vào thư mục đó
class GroupFileByFirstLetter(Folder):
    def __init__(self, path):
        super().__init__(path)
        self.group_files()

    def group_files(self):
        for file in self.files:
            name, extension = os.path.splitext(file)
            first_letter = str(name[0]).upper()
            if not os.path.exists(os.path.join(self.path, first_letter)):
                os.mkdir(os.path.join(self.path, first_letter))

            try:
                shutil.move(os.path.join(self.path, file), os.path.join(self.path, first_letter, file))
                # os.rename(os.path.join(self.path, file), os.path.join(self.path, first_letter, file))
            except Exception as e:
                print(f'Error: {file}', e)
            
# group = GroupFileByFirstLetter(path)
# group.group_files()

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
            date = str(date).split(' ')[0].strip()
            if not os.path.exists(os.path.join(self.path, date)):
                os.mkdir(os.path.join(self.path, date))
            try:
                shutil.move(os.path.join(self.path, file), os.path.join(self.path, date, file))
                # os.rename(os.path.join(self.path, file), os.path.join(self.path, date, file))
            except Exception as e:
                print(f'Error: {file}', e)

# group = GroupFileByDateDownload(path)
# group.group_files()
vi_tri_cut_name = {"bat_dau": 1, "ket_thuc": None}
if vi_tri_cut_name['bat_dau'] and vi_tri_cut_name['ket_thuc']:
    print('ok')
else:
    print("no")

    