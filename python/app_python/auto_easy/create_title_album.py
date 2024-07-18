import os
import shutil
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TALB
from change_file import Folder

path ='D:\\music\\loa pháp thoại\\001 HT Thiền Sư Thích Nhất Hạnh'
path = os.path.normpath(path)
folder_ob = Folder(path)
print(folder_ob.folders)

folders = folder_ob.folders
for folder in folders:
    path_folder = os.path.join(path, folder)
    folder_ob = Folder(path_folder)
    print(folder_ob.files)
    for file in folder_ob.files:
        try: 
            file_path = os.path.join(path_folder, file)
            name, extension = os.path.splitext(file)
            audio = MP3(file_path, ID3=ID3)
            # thêm thẻ ID3 nếu chưa có
            if audio.tags is None:
                audio.add_tags()
            # thay đổi title và album
            audio.tags.add(TIT2(encoding=3, text=name))
            audio.tags.add(TALB(encoding=3, text='HT Thiền Sư Thích Nhất Hạnh'))
            audio.save()
            print("Metadata updated successfully: ", audio.get('TIT2'), audio.get('TALB'))
        except Exception as e:
            print(e)


    