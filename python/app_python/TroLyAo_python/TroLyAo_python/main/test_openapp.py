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

def open_application(): #!!!
    Mouth.speak("bạn muốn mở gì ạ")
    text = hieu.get_text()
    try:
        if "google" in text:
            os.startfile(
                'C:\\Program Files\\Google\Chrome\\Application\\chrome.exe')
        elif "microsoft" in text:
            os.startfile(
                'C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge.exe')
        elif "ổ c" in text:
            os.startfile(
                'C:')
        elif "tài liệu" in text:
            os.startfile(
                'C:\\Users\\lea81\\Documents')
        elif "máy tính bàn" in text:
            os.startfile(
                'C:\\Users\\lea81\\Links\\Desktop')
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

def assistant():
    Mouth.speak("Trợ lý chân thiện tâm Xin chào, bạn tên là gì nhỉ?")
    name = hieu.get_text()
    print(f"name: {name}")
    if name:
        Mouth.speak("Xin chào {}".format(name))
        Mouth.speak(f"{name} cần thiện tâm giúp gì ạ?")
        while True:
            text = hieu.get_text()
            print("text: " + text)
            if not text:
                break
            elif "dừng" in text or "tạm biệt" in text or "chào robot" in text or "kết thúc" in text:
                Stop.stop()
                break
            # elif "có thể làm gì" in text or "giúp" in text:
            #     help_me()
            # elif "chào" in text:
            #     hello(name)
            # elif "hôm nay" in text or "bây giờ" in text:
            #     get_time(text)
            elif "mở" in text:  
                open_application()
            elif 'website' in text or 'lên mạng' in text:
                open_website()
            elif "đóng" in text:
                close_application(text)

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

assistant()