import os
import shutil
from abc import ABC, abstractmethod
from change_file import Folder

class GroupFile(Folder):
    def __init__(self, path, logger=None):
        super().__init__(path)
        self.logger = logger

    @abstractmethod
    def group_files(self):
        pass


# nhóm file theo đuôi: 
class GroupFileByExtension(GroupFile):
    def __init__(self, path, logger=None):
        super().__init__(path, logger)

    def group_files(self):
        for file in self.files:
            name, extension = os.path.splitext(file)
            if not os.path.exists(os.path.join(self.path, extension)):
                os.mkdir(os.path.join(self.path, extension))
            try:
                shutil.move(os.path.join(self.path, file), os.path.join(self.path, extension, file))
                self.logger.write(f'Move file {file} to folder {extension}')
                # os.rename(os.path.join(self.path, file), os.path.join(self.path, extension, file))
            except Exception as e:
                self.logger.write(f'Error: {file}', e)

# nhóm file theo ky tu dau tien: tạo thư mục theo ky tu dau tien và di chuyen file vào thư mục đó
class GroupFileByFirstLetter(GroupFile):
    def __init__(self, path, logger=None):
        super().__init__(path, logger)

    def group_files(self):
        for file in self.files:
            name, extension = os.path.splitext(file)
            first_letter = str(name[0]).upper()
            if not os.path.exists(os.path.join(self.path, first_letter)):
                os.mkdir(os.path.join(self.path, first_letter))

            try:
                shutil.move(os.path.join(self.path, file), os.path.join(self.path, first_letter, file))
                self.logger.write(f'Move file {file} to folder {first_letter}')
                # os.rename(os.path.join(self.path, file), os.path.join(self.path, first_letter, file))
            except Exception as e:
                self.logger.write(f'Error: {file}', e)
   
# nhóm file theo ngay download: tạo thư mục theo ngay download và di chuyen file vào thư mục đó
from datetime import datetime
class GroupFileByDateDownload(GroupFile):
    def __init__(self, path, logger=None):
        super().__init__(path, logger)

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
                self.logger.write(f'Move file {file} to folder {date}')
                # os.rename(os.path.join(self.path, file), os.path.join(self.path, date, file))
            except Exception as e:
                self.logger.write(f'Error: {file}', e)

