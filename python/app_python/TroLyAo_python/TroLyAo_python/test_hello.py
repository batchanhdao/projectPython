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


def hello(name):
    day_time = int(strftime('%H'))
    print(day_time)
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))

hello('Ánh')


def get_time(text):
    now = datetime.datetime.now()
    print(now)
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        speak("Bot chưa hiểu ý của bạn. Bạn nói lại được không?")

get_time("Mấy giờ rồi")