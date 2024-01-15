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
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("C:\\Users\\lea81\\Downloads\\TroLyAo_python\\lehonganh.mp3")
    playsound.playsound("C:\\Users\\lea81\\Downloads\\TroLyAo_python\\lehonganh.mp3", True)
    time.sleep(0.1)
    os.remove("C:\\Users\\lea81\\Downloads\\TroLyAo_python\\lehonganh.mp3")

speak("Xin chào quản trị viên")

def stop():
    speak("Hẹn gặp lại bạn sau!")

def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Bot không nghe rõ. Bạn nói lại được không!")
    time.sleep(2)
    stop()
    return 0

def open_website(text):
    if 'mở' in text:
        reg_ex = text.split("mở", 1)[1].strip()
        if len(reg_ex)==0: 
            speak('bạn muốn mở website nào')
            reg_ex = get_text.split('mở',1)[1].strip()
        if '.' in reg_ex:
            domain = reg_ex
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            speak('{} đã được mở'.format(domain))
            return True
        else:
            domain = reg_ex
            print(domain)
            url = 'https://www.google.com/search?q=' + domain
            webbrowser.open(url)
            speak('{} đã được mở'.format(domain))
    elif 'kiếm' in text:
        reg_ex = text.split("kiếm", 1)[1].strip()
        if 'trên' in reg_ex and 'youtube' in reg_ex:
            name = reg_ex.rsplit('trên',1)[0].strip()
            print(name )
            domain = '+'.join(name.split())
            print(domain)
            url = 'https://www.youtube.com/results?search_query=' + domain
            webbrowser.open(url)
            speak('{} đã được tìm'.format(name))
        else:
            domain = reg_ex
            print(domain)
            url = 'https://www.google.com/search?q=' + domain
            webbrowser.open(url)
            speak('{} đã được tìm'.format(domain))

    # reg_ex = re.search('mở (.+)', text)
    # if reg_ex:
    #     domain = reg_ex.group(1)
    #     url = 'https://www.' + domain
    #     webbrowser.open(url)
    #     speak("Trang web bạn yêu cầu đã được mở.")
    #     return True
    # else:
    #     return False
# open_website('mở youtube')
# open_website('mở sách hay')
open_website('mở youtube.com')
open_website('hãy kiếm trần việt quân trên youtube')
open_website('kiếm trần việt quân')

