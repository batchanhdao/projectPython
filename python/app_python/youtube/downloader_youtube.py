from yt_dlp import YoutubeDL
import os
import json
from datetime import datetime

# Thiết lập thư mục làm việc
working_directory = os.getcwd()
# Đặt thư mục làm việc
os.chdir(working_directory)

class Video:
    def __init__(self, urls, quality=0):
        self.urls = urls
        if quality == 1080:
            self.ydl_opts = {
                'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            }
        elif quality == 720:
            self.ydl_opts = {
                'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            }
        elif quality == 480:
            self.ydl_opts = {
                'format': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
            }
        else:
            self.ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
            }
    
    def download(self):
        with YoutubeDL(self.ydl_opts) as ydl:
            ydl.download(self.urls)

class Audio:
    def __init__(self, urls, preferredcodec="mp3", preferredquality="192"):
        self.urls = urls
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': preferredcodec,
                'preferredquality': preferredquality,
            }],
        }
    
    def download(self):
        with YoutubeDL(self.ydl_opts) as ydl:
            ydl.download(self.urls)

class File:
    def __init__(self, urls):
        self.urls = urls
        
    def write(self):
        file_name = f"info_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
        for url in self.urls:
            try:
                with YoutubeDL() as ydl:
                    info = ydl.extract_info(url, download=False)
                    data = {}
                    data['url'] = url
                    data['title'] = info.get('title', "No title")
                    data['thumbnail'] = info.get('thumbnail', "No thumbnail")
                    data['channel'] = info.get('channel', "No channel")
                    data['channel_url'] = info.get('channel_url', "No channel URL")
                    requested_formats = info.get('requested_formats', "No requested formats")
                    if type(requested_formats) == list:
                        data['url_video'] = requested_formats[0].get('url', "No video URL")
                        data['url_audio'] = requested_formats[1].get('url', "No audio URL")
                    with open(file=file_name, mode='a', encoding="UTF-8") as f:
                        data_json = json.dumps(data)
                        f.write(data_json)
                        f.write("\n")
            except Exception as e:
                print("Error:", e)
                continue

def go_to_folder(name_folder=""):
    folder_path = os.path.join(working_directory, name_folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    os.chdir(folder_path)
    
def main():
    video_urls = []
    while True:
        try:
            # Hiển thị thông điệp hướng dẫn để người dùng nhập URL video hoặc 'ex' để kết thúc chương trình.
            print("Bấm Share trên Youtube để lấy URL")
            print("""
            Nhập 'URL của Video' để tải video
                    hoặc 
            'ex' để đóng chương trình
                    hoặc
            'ok' để thực hiện tải: """)
            text = input().strip()
            # Kiểm tra nếu người dùng nhập 'ex', thoát khỏi vòng lặp
            if text == 'ex':
                return
            
            elif text == 'ok':
                try:
                    go_to_folder('info')
                    file = File(urls=video_urls)
                    file.write()
                    # Hiển thị các lựa chọn cho người dùng
                    print("""Options: 
                        '1' to get audio
                        '2' to get video
                        """)
                    # Nhập lựa chọn từ người dùng
                    option = input("Enter your choice: ").strip()
                    if option == '1':
                        go_to_folder('audio')
                        print("Chọn loại file audio muốn tải: ")
                        print("mp3")
                        print("m4a")
                        print("wav")
                        print("webm")
                        preferredcodec = input("Enter your choice: ").strip().lower()
                        print("Downloading audio...")
                        audio = Audio(urls=video_urls, preferredcodec=preferredcodec)
                        audio.download()
                        
                    elif option == '2':
                        go_to_folder('video')
                        print("Chọn chất lượng video muốn tải: ")
                        print("'1080': Tối đa 1080")
                        print("'720': Tối đa 720")
                        print("'480': Tối đa 480")
                        print("'0': Tốt nhất")
                        quantity = int(input("Enter your choice: ").strip())
                        print("Downloading video...")
                        video = Video(urls=video_urls, quality=quantity)
                        video.download()
                        
                    else:
                        # Hiển thị thông điệp nếu người dùng chọn một lựa chọn không hợp lệ
                        print("Unknown option!")
                        
                except Exception as e:
                    print("Error:", e)
                
            else:
                video_urls.append(text)
                print('URL:', video_urls)
                
        except Exception as e:
            print("Error:", e)
            
            

# Kiểm tra nếu đây là file chính
if __name__ == "__main__":
    print(f"Current working directory: {working_directory}")
    main()
    
    