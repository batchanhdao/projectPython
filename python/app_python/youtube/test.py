from yt_dlp import YoutubeDL
import os
import json

x = 1955
th = 12
print(x%th)
# 1958: 2 -> +9/-3, 

# Thiết lập thư mục làm việc
# working_directory = os.getcwd()
# print(working_directory)
# # os.chdir(working_directory)
# def path():
#     folder = 'app_python'
#     folder_path = os.path.join(working_directory, folder)
#     os.chdir(folder_path)
#     print(working_directory)

# path()
# print(working_directory)
    
# URLS = ['https://www.youtube.com/watch?v=iB7f5JUZD_w']
# with YoutubeDL() as ydl:
#     ydl.download(URLS)
# URL = 'https://www.youtube.com/watch?v=iB7f5JUZD_w'
# ydl_opts = {}
# with YoutubeDL(ydl_opts) as ydl:
#     info = ydl.extract_info(URL, download=False)

#     # ℹ️ ydl.sanitize_info makes the info json-serializable
#     # print(json.dumps(ydl.sanitize_info(info)))
#     info_json = json.dumps(ydl.sanitize_info(info))
#     url_video = info['requested_formats'][0]['url']
#     print(url_video)
#     print(type(url_video))
#     url_audio = info['requested_formats'][1]['url']
#     print(url_audio)
#     print(type(url_audio))
    # with open('info.json', 'w') as f:
    #     f.write(url)
    
    
#     Extract audio
# import yt_dlp

# URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']

# ydl_opts = {
#     'format': 'm4a/bestaudio/best',
#     # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
#     'postprocessors': [{  # Extract audio using ffmpeg
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'm4a',
#     }]
# }

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     error_code = ydl.download(URLS)