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
import pyaudio

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



def assistant():
    Mouth.speak("Trợ lý chân thiện tâm Xin chào, bạn tên là gì nhỉ?")
    # name = hieu.get_text()
    name='ánh'
    if name:
        Mouth.speak("Xin chào {}".format(name))
        while True:
            Mouth.speak(f"{name} cần thiện tâm giúp gì không ạ?")
            text = hieu.get_text()
            if not text:
                break
            elif 'không' in text or 'chưa' in text:
                time.sleep(60*3)
            elif "dừng" in text or "tạm biệt" in text or "chào robot" in text or "kết thúc" in text:
                Stop.stop()
                break
            # elif "có thể làm gì" in text or "giúp" in text:
            #     help_me()
            # elif "chào" in text:
            #     hello(name)
            # elif "hôm nay" in text or "bây giờ" in text:
            #     get_time(text)
            # elif "mở" in text:  
            #     open_application()
            # elif 'website' in text or 'lên mạng' in text:
            #     open_website()
            # elif "đóng" in text:
            #     close_application(text)

            # elif "email" in text or "mail" in text or "gmail" in text:
            #     send_email(text)
            elif "chơi nhạc" in text:
                play_song()
            elif "hình nền" in text:
                change_wallpaper()
            elif "đọc báo" in text:
                read_news()
            else:
                Mouth.speak("thiện tâm không hiểu, bạn nói lại được không")
                

assistant()