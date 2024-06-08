import os
from change_file import Folder

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
            except Exception as e:
                print(f'Error: {file}', e)

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
            except Exception as e:
                print(f'Error: {file}', e)
            
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
            except Exception as e:
                print(f'Error: {file}', e)
    