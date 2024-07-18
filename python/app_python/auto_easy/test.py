import os
import shutil
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TALB
from change_file import Folder

vi_tri_remove_text = -1
len_remove_text = 10
name = 'example_file'
if vi_tri_remove_text < 0 or len_remove_text <= 0:
    print('Error')
if vi_tri_remove_text > len(name):
    print('Error')
if vi_tri_remove_text == 0:
    name = name[0: len(name) - len_remove_text]
if vi_tri_remove_text > 0:
    if vi_tri_remove_text + len_remove_text - 1 > len(name):
        len_remove_text = len(name) - vi_tri_remove_text + 1
    name = name[0: vi_tri_remove_text - 1] + name[vi_tri_remove_text + len_remove_text - 1:]
print(name)

# path ='D:\\music\\loa pháp thoại\\003 đức đạt lai lạc ma'
# path = os.path.normpath(path)
# folder_ob = Folder(path)
# print(folder_ob.folders)

# folders = folder_ob.folders
# for folder in folders:
#     path_folder = os.path.join(path, folder)
#     folder_ob = Folder(path_folder)
#     print(folder_ob.files)
#     for file in folder_ob.files:
#         file_path = os.path.join(path_folder, file)
#         name, extension = os.path.splitext(file)
#         audio = MP3(file_path, ID3=ID3)
#         if audio.tags is None:
#             audio.add_tags()
#         audio.tags.add(TIT2(encoding=3, text=name))
#         audio.tags.add(TALB(encoding=3, text='Duc Dat Lai Lac Ma'))
#         audio.save()
#         print("Metadata updated successfully.")

# # Đường dẫn đến file MP3 của bạn
# file_path = 'example.mp3'

# # Mở file MP3
# audio = MP3(file_path, ID3=ID3)

# # Thêm thẻ ID3 nếu chưa có
# if audio.tags is None:
#     audio.add_tags()

# # Thay đổi title và album
# audio.tags.add(TIT2(encoding=3, text='My New Title'))
# audio.tags.add(TALB(encoding=3, text='My New Album'))

# # Lưu thay đổi
# audio.save()

# print("Metadata updated successfully.")


    