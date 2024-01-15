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

def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        Mouth.speak("Chào buổi sáng {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        Mouth.speak("Chào buổi chiều {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        Mouth.speak("Chào buổi tối {}. Bạn đã nghỉ ngơi chưa nhỉ.".format(name))
    time.sleep(1)

def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        Mouth.speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        Mouth.speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        Mouth.speak("Thiện tâm chưa hiểu ý của bạn. Bạn nói lại được không?")
    time.sleep(1)

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
    time.sleep(1)
    name = hieu.get_text()
    print(f"name: {name}")
    if name:
        Mouth.speak("Xin chào {}".format(name))
        Mouth.speak(f"{name} cần thiện tâm giúp gì ạ?")
        time.sleep(1)
        while True:
            text = hieu.get_text()
            print("text: " + text)
            if not text:
                break
            elif "dừng" in text or "tạm biệt" in text or "chào robot" in text or "kết thúc" in text:
                Stop.stop()
                break
            elif "có thể làm gì" in text or "giúp" in text:
                help_me()
            elif "chào" in text:
                hello(name)
            elif "hôm nay" in text or "bây giờ" in text:
                get_time(text)
            # elif "mở" in text:  #!!!
            #     if 'tìm kiếm' in text:
            #         open_website(text)
            #     else:
            #         open_application(text)
            # elif "email" in text or "mail" in text or "gmail" in text:
            #     send_email(text)
            # elif "chơi nhạc" in text:
            #     play_song()
            # elif "hình nền" in text:
            #     change_wallpaper()
            # elif "đọc báo" in text:
            #     read_news()
            else:
                Mouth.speak(f"{name} cần thiện tâm giúp gì ạ?")
                time.sleep(1)

assistant()