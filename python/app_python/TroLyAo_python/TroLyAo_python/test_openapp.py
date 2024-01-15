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
import smtplib
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

wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()

def speak(text):
    print("Trợ lý Chân Thiện Tâm: {}".format(text))
    tts = gTTS(text="Trợ lý Chân Thiện Tâm"+text, lang=language, slow=False)
    tts.save("C:\\Users\\lea81\\Downloads\\TroLyAo_python\\lehonganh.mp3")
    playsound.playsound("C:\\Users\\lea81\\Downloads\\TroLyAo_python\\lehonganh.mp3", True)
    time.sleep(0.1)
    os.remove("C:\\Users\\lea81\\Downloads\\TroLyAo_python\\lehonganh.mp3")

speak("Xin chào quản trị viên")

def open_application(text):
    if "google" in text:
        speak("Mở Google Chrome")
        os.startfile(
            'C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif "edge" in text:
        speak("Mở Microsoft edge")
        os.startfile(
            'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
    elif "ổ c" in text:
        speak("Mở ổ c")
        os.startfile(
            'C:')
    elif "tài liệu" in text:
        speak("Mở tài liệu")
        os.startfile(
            'C:\\Users\\lea81\\Documents')
    elif "máy tính bàn" in text:
        speak("máy tính bàn")
        os.startfile(
            'C:\\Users\\lea81\\Links\\Desktop')
    elif "nhạc" in text:
        speak("mở nhạc")
        path='C:\\Users\\lea81\\Music'
        for file in os.listdir(path):
            if file.endswith('.mp3'):
                print(file)
                os.startfile(path+'\\'+file)
                time.sleep(10)
                subprocess.call("TASKKILL /F /IM Music.UI.exe",shell=True)
    elif "ảnh" in text:
        speak("mở ảnh")
        path='C:\\Users\\lea81\\Pictures'
        for file in os.listdir(path):
            if file.endswith('.png') or file.endswith('jpg'):
                print(file)
                os.startfile(path+'\\'+file)
                time.sleep(10)
                subprocess.call("TASKKILL /F /IM Microsoft.Photos.exe",shell=True)
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")

def close_application(text):
    if "google" in text:
        speak("đóng Google Chrome")
        subprocess.call("TASKKILL /F /IM chrome.exe",shell=True)
    elif "edge" in text:
        speak("đóng Microsoft edge")
        subprocess.call("TASKKILL /F /IM msedge.exe",shell=True)
    elif "máy tính bàn" in text:
        subprocess.call("TASKKILL /F /IM explorer.exe",shell=True)
    elif "nhạc" in text:
        subprocess.call("TASKKILL /F /IM Music.UI.exe",shell=True)
    elif "ảnh" in text:
        subprocess.call("TASKKILL /F /IM Microsoft.Photos.exe",shell=True)
    else:
        speak("Ứng dụng chưa được mở. Bạn hãy thử lại!")
# open_application('hãy mở google')
# open_application('bật nhạc')
# open_application('mở ổ c')
# open_application('Mở tài liệu')
open_application('Mở máy tính bàn')
# open_application('mở ảnh')
# open_application('hãy mở edge')

# close_application('tắt nhạc')
# close_application('đóng google')
close_application('máy tính bàn')

