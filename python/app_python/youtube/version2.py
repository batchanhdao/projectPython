
import pytube
import os

# Thiết lập thư mục làm việc
# working_directory = os.getcwd()
working_directory = r'D:\pythonProject\python\app_python\youtube\download_video'

# Hàm download_video(stream) nhận một đối tượng stream và thực hiện việc tải video dựa trên stream đó.
def download_video(stream):
    try:
        # Hiển thị thông báo bắt đầu quá trình tải video
        print("---------Please Wait for Download to Finish---------")
        # Sử dụng phương thức download() của stream để tải video
        stream.download()
        # Hiển thị thông báo tải video thành công
        print("---------Download Success--------")
    except Exception as e:
        # Xử lý ngoại lệ nếu có lỗi xảy ra trong quá trình tải video
        print("------------Error------------")
        print(e)

# Hàm go_to_folder(name_folder="") chuyển đến thư mục được chỉ định và tạo thư mục nếu nó không tồn tại.
def go_to_folder(name_folder=""):
    folder_path = os.path.join(working_directory, name_folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    os.chdir(folder_path)


# Hàm main() là hàm chính của chương trình, thực hiện quá trình chọn và tải video từ YouTube.
def main():
    
    while True:
        os.chdir(working_directory)
        urls = []
        # Hiển thị thông điệp hướng dẫn để người dùng nhập URL video hoặc 'ex' để kết thúc chương trình.
        print("Click Share on Youtube to get URL")
        print("ENTER VIDEO URLS then Click 'ok' or 'ex' to END:")
        while True:
            video_url = input().strip()
            if video_url == 'ex':
                return
            elif video_url == 'ok':
                break
            else:
                urls.append(video_url)
        print("-----------urls:--------")
        print("\n".join(urls))
        # Hiển thị các lựa chọn cho người dùng
        print("""Options: 
            '1' to get audio
            '2' to get video highest
            '3' to get video lowest""")
        # Nhập lựa chọn từ người dùng
        option = input("Enter your choice: ").strip()

        for url in urls:
            try:
                # Tạo một đối tượng YouTube từ URL được nhập
                yt = pytube.YouTube(url)

                if option == '1':
                    # Nếu người dùng chọn '1', lấy đối tượng stream chỉ chứa âm thanh
                    stream = yt.streams.get_audio_only()
                    # gọi hàm go_to_folder() để chuyển đến thư mục được chỉ định
                    go_to_folder('audio') 
                    # Gọi hàm download_video() để tải video dựa trên stream âm thanh
                    download_video(stream)
                elif option == '2':
                    # Nếu người dùng chọn '2', lấy đối tượng stream có độ phân giải cao nhất
                    stream = yt.streams.get_highest_resolution()
                    # gọi hàm go_to_folder() để chuyển đến thư mục được chỉ định
                    go_to_folder('video')
                    # Gọi hàm download_video() để tải video dựa trên stream có độ phân giải cao nhất
                    download_video(stream)
                elif option == '3':
                    # Nếu người dùng chọn '3', lấy đối tượng stream có độ phân giải thấp nhất
                    stream = yt.streams.get_lowest_resolution()
                    # gọi hàm go_to_folder() để chuyển đến thư mục được chỉ định
                    go_to_folder('video')
                    # Gọi hàm download_video() để tải video dựa trên stream có độ phân giải thấp nhất
                    download_video(stream)
                else:
                    # Hiển thị thông điệp nếu người dùng chọn một lựa chọn không hợp lệ
                    print("Unknown option!")

            except Exception as e:
                # Xử lý ngoại lệ nếu có lỗi xảy ra trong quá trình xử lý lựa chọn
                print("Error:", e)


# Kiểm tra nếu đây là file chính và chạy hàm main()
if __name__ == "__main__":
    print(f"Current working directory: {working_directory}")
    main()
    
    
