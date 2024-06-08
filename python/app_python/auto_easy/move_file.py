import os
from datetime import datetime
from change_file import Folder

   
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
