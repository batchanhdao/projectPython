import os
import playsound
import speech_recognition as sr
import sys
import ctypes
import wikipedia
import datetime
import time
import json
import re
import webbrowser
import smtplib, ssl
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
import subprocess
#----------------------------------------------
import Understand as hieu
import Mouth
import Stop


def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        Mouth.speak("Chào buổi sáng {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        Mouth.speak("Chào buổi chiều {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        Mouth.speak("Chào buổi tối {}. Bạn đã nghỉ ngơi chưa nhỉ.".format(name))

def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        Mouth.speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        Mouth.speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        Mouth.speak("Thiện tâm chưa hiểu ý của bạn. Bạn nói lại được không?")

def open_application(): #!!!
    Mouth.speak("bạn muốn mở gì ạ")
    text = hieu.get_text()
    try:
        if "google" in text:
            os.startfile(
                'C:\\Program Files\\Google\Chrome\\Application\\chrome.exe'
                # 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
                )
        elif "microsoft" in text:
            os.startfile(
                'C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge.exe'
                # 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
                )
        elif "word" in text or "soạn thảo" in text:
            os.startfile(
                # 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
                )
        elif "powerpoint" in text or "trang trình bày" in text:
            os.startfile(
                # 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
                )
        elif "excel" in text or "trang tính" in text:
            os.startfile(
                # 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
                )
        elif "outlook" in text :
            os.startfile(
                # 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE'
                )
        elif "access" in text :
            os.startfile(
                # 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSACCESS.EXE'
                )
        elif "điều khiển máy tính" in text :
            os.startfile(
                # 'C:\\Program Files (x86)\\UltraViewer\\UltraViewer_Desktop.exe'
                )
        elif "đọc pdf" in text :
            os.startfile(
                # 'C:\\Program Files (x86)\\Foxit Software\\Foxit Reader\\FoxitReader.exe'
                )
        elif "zoom" in text:
            os.startfile(
                # 'C:\\Users\\Admin\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
                )
        elif "gõ chữ" in text:
            os.startfile(
                # 'C:\\Program Files\\EVKey\\EVKey.exe'
                )
        elif "github" in text:
            os.startfile(
                # 'C:\\Users\\Admin\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe'
                )
        elif "máy ảo" in text:
            os.startfile(
                # 'C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe'
                )
        elif "sql" in text:
            os.startfile(
                # 'C:\\Program Files\\MySQL\\MySQL Workbench 8.0 CE\\MySQLWorkbench.exe'
                )
        elif "netbean" in text:
            os.startfile(
                # 'C:\\Program Files\\NetBeans-14\\netbeans\\bin\\netbeans64.exe'
                )
        elif "pycharm" in text:
            os.startfile(
                # 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.3\\bin\\pycharm64.exe'
                )
        elif "code" in text:
            os.startfile(
                # 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                )
        elif "notepad" in text:
            os.startfile(
                # 'C:\\Windows\\System32\\notepad.exe'
                )
        elif "ổ c" in text:
            os.startfile(
                'C:')
        elif "ổ d" in text:
            os.startfile(
                # 'D:'
                )
        elif "tài liệu" in text:
            os.startfile(
                'C:\\Users\\lea81\\Documents')
        elif "admin" in text:
            os.startfile(
                'C:\\Users\\Admin')
        elif "nhạc" in text:
            path='C:\\Users\\lea81\\Music'
            for file in os.listdir(path):
                if file.endswith('.mp3'):
                    print(file)
                    os.startfile(path+'\\'+file)
                    time.sleep(100)
                    # subprocess.call("TASKKILL /F /IM Music.UI.exe",shell=True)
        elif "ảnh" in text:
            path='C:\\Users\\lea81\\OneDrive\\Pictures'
            for file in os.listdir(path):
                if file.endswith('.png') or file.endswith('jpg'):
                    print(file)
                    os.startfile(path+'\\'+file)
                    time.sleep(10)
                    # subprocess.call("TASKKILL /F /IM Microsoft.Photos.exe",shell=True)
        else:
            return Mouth.speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
    except Exception as e:
        print(e)
        return Mouth.speak("đã xảy ra lỗi")
    return  Mouth.speak(f"đã mở {text}")

def close_application(text):
    try:
        if "google" in text:
            subprocess.call("TASKKILL /F /IM chrome.exe",shell=True)
        elif "microsoft" in text:
            subprocess.call("TASKKILL /F /IM msedge.exe",shell=True)
        elif "nhạc" in text:
            subprocess.call("TASKKILL /F /IM Music.UI.exe",shell=True)
        elif "ảnh" in text:
            subprocess.call("TASKKILL /F /IM Microsoft.Photos.exe",shell=True)
        else:
            return Mouth.speak("Ứng dụng chưa được mở. Bạn hãy thử lại!")
    except Exception as e:
        print(e)
        return Mouth.speak("đã xảy ra lỗi")
    return Mouth.speak(f"đã {text}")

def open_website():
    Mouth.speak("bạn muốn làm gì trên mạng")
    text = hieu.get_text()
    if 'mở' in text:
        reg_ex = text.split("mở", 1)[1].strip()
        if len(reg_ex)==0: 
            Mouth.speak('bạn muốn mở website nào')
            reg_ex = hieu.get_text().split('mở',1)[1].strip()
        if '.' in reg_ex:
            domain = reg_ex
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            Mouth.speak('{} đã được mở'.format(domain))
            return True
        else:
            domain = reg_ex
            print(domain)
            url = 'https://www.google.com/search?q=' + domain
            webbrowser.open(url)
            Mouth.speak('{} đã được mở'.format(domain))
    elif 'kiếm' in text:
        reg_ex = text.split("kiếm", 1)[1].strip()
        if 'trên' in reg_ex and 'youtube' in reg_ex:
            name = reg_ex.rsplit('trên',1)[0].strip()
            print(name )
            domain = '+'.join(name.split())
            print(domain)
            url = 'https://www.youtube.com/results?search_query=' + domain
            webbrowser.open(url)
            Mouth.speak('{} đã được tìm'.format(name))
        else:
            domain = reg_ex
            print(domain)
            url = 'https://www.google.com/search?q=' + domain
            webbrowser.open(url)
            Mouth.speak('{} đã được tìm'.format(domain))

def send_email(text):#!!!
    import Send_Message as send
    ds_nguoi_nhan = {}
    while True:
        Mouth.speak('Bạn gửi email cho ai nhỉ')
        receivers_email = hieu.get_text()
        Mouth.speak("Tiêu đề là gì ạ")
        subject=hieu.get_text()
        Mouth.speak('Nội dung bạn muốn gửi là gì')
        body = hieu.get_text()
        Mouth.speak("mời bạn xác nhận lại")
        check = hieu.get_text()
        if 'ok' in check or 'tiếp' in check or 'gửi' in check:
            if "và" in receivers_email:
                receivers_email=receivers_email.split('và')
                for receiver_email in receivers_email:
                    if receiver_email in ds_nguoi_nhan:
                        send.send_gmail(ds_nguoi_nhan[receiver_email],subject,body)
                    else:
                        Mouth.speak('thiện tâm không hiểu bạn muốn gửi email cho ai')
            else:
                if receiver_email in ds_nguoi_nhan:
                    send.send_gmail(ds_nguoi_nhan[receiver_email],subject,body)
                else:
                    Mouth.speak('thiện tâm không hiểu bạn muốn gửi email cho ai')
            Mouth.speak('bạn có muốn tiếp tục gửi tin không')
            check = hieu.get_text()
            if 'có' in check or 'tiếp' in check:
                Mouth.speak('tiếp tục gửi tin')
            else:
                return Mouth.speak("quá trình gửi tin đã kết thúc")
        else:
            return Mouth.speak("quá trình gửi đã được hủy")

def play_song():
    try:
        Mouth.speak('Bạn muốn nghe gì ạ')
        mysong = hieu.get_text()
        while True:
            result = YoutubeSearch(mysong, max_results=10).to_dict()
            if result:
                break
        url = 'https://www.youtube.com' + result[0]['url_suffix']
        webbrowser.open(url)
    except Exception as e:
        print(e)
        return Mouth.speak('đã xảy ra lỗi')
    Mouth.speak("Bài hát bạn yêu cầu đã được mở.")
    time.sleep(100)
    return 

def change_wallpaper():  #!!!
    try:
        api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
        url = 'https://api.unsplash.com/photos/random?client_id=' + \
            api_key  # pic from unspalsh.com
        f = urllib2.urlopen(url)
        json_string = f.read()
        f.close()
        parsed_json = json.loads(json_string)
        photo = parsed_json['urls']['full']
        # Location where we download the image to.
        urllib2.urlretrieve(photo, "C:/Users/lea81/Downloads/a2.png")
        image=os.path.join("C:/Users/lea81/Downloads/a2.png")
        # urllib2.urlretrieve(photo, "C:/Users/admin/Downloads/a.png")
        # image=os.path.join("C:/Users/admin/Downloads/a.png")
        ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
        
    except Exception as e:
        Mouth.speak("đã xảy ra lỗi")
        print(e)
    return Mouth.speak('Hình nền máy tính vừa được thay đổi')

def read_news():
    Mouth.speak("Bạn muốn đọc báo về gì")
    theme = hieu.get_text()
    try:
        if theme =="" or "để xem" in theme:
            url = "https://news.google.com/home?hl=vi&gl=VN&ceid=VN:vi"
        else:
            text = str(theme).strip().replace('  ',' ')
            text = text.replace(' ','%20')
            url = f"https://news.google.com/search?q={text}&hl=vi&gl=VN&ceid=VN%3Avi"
        webbrowser.open(url)
    except Exception as e:
        print(e)
        return Mouth.speak('đã xảy ra lỗi')
    return Mouth.speak('bài báo bạn muốn đã được mở')

def help_me():
    Mouth.speak("""Thiện tâm có thể giúp bạn thực hiện các chức năng sau đây:
    1. Chào hỏi
    2. Hiển thị giờ
    3. Mở website, application
    4. Tìm kiếm trên Google
    5. Gửi email
    6. Mở video nhạc
    7. Thay đổi hình nền máy tính
    8. Đọc báo hôm nay""")
    time.sleep(12)


def assistant():
    Mouth.speak("Trợ lý chân thiện tâm Xin chào, bạn tên là gì nhỉ?")
    # name = hieu.get_text()
    name='ánh'
    if name:
        Mouth.speak("Xin chào {}".format(name))
        while True:
            Mouth.speak(f"{name} cần thiện tâm giúp gì không ạ?")
            text = hieu.get_text()
            if 'không' in text or 'chưa' in text or 'sleep' in text:
                time.sleep(60*3)
            elif "dừng" in text or "tạm biệt" in text or "chào robot" in text or "kết thúc" in text:
                return Stop.stop()
            elif "có thể làm gì" in text or "giúp" in text:
                help_me()
            elif "chào" in text:
                hello(name)
            elif "hôm nay" in text or "bây giờ" in text:
                get_time(text)
            elif "mở" in text:  
                open_application()
            elif 'website' in text or 'lên mạng' in text:
                open_website()
            elif "đóng" in text:
                close_application(text)
            elif "email" in text or "mail" in text or "gmail" in text:
                send_email(text)
            elif "chơi nhạc" in text:
                play_song()
            elif "hình nền" in text:
                change_wallpaper()
            elif "đọc báo" in text:
                read_news()
            else:
                Mouth.speak("thiện tâm không hiểu, bạn nói lại được không")
                

assistant()
