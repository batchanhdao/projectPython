import os
import playsound
import speech_recognition as sr
import ctypes
import wikipedia
import time
import json
import re
import webbrowser
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS

wikipedia.set_lang('vi')
language = 'vi'
# path = ChromeDriverManager().install()

def speak(text):
    print("Trợ lý Chân Thiện Tâm: {}".format(text))
    tts = gTTS(text="Trợ lý Chân Thiện Tâm"+text, lang=language, slow=False)
    tts.save("C:\\Users\\lea81\\Downloads\\TroLyAo_python\\lehonganh.mp3")
    playsound.playsound("C:\\Users\\lea81\\Downloads\\TroLyAo_python\\lehonganh.mp3", True)
    time.sleep(0.1)
    os.remove("C:\\Users\\lea81\\Downloads\\TroLyAo_python\\lehonganh.mp3")

speak("Xin chào quản trị viên")

def change_wallpaper():
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
        speak('Hình nền máy tính vừa được thay đổi')
    except Exception as e:
        speak("đã xảy ra lỗi")
        print(e)

change_wallpaper()