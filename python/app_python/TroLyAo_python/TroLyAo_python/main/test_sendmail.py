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

def send_email(text):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    smtp_server = "smtp.gmail.com"
    sender_email = "lea81807@gmail.com"  # Enter your address
    password = 'hqenlurtqbhpedka'
    Mouth.speak('Bạn gửi email cho ai nhỉ')
    receiver_email = hieu.get_text()
    path = "anhle12341710@gmail.com"
    if 'tôi' in receiver_email:
        try:
            Mouth.speak("Tiêu đề là gì ạ")
            subject=hieu.get_text()
            Mouth.speak('Nội dung bạn muốn gửi là gì')
            body = hieu.get_text()
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = path
            message["Subject"] = subject
            message["Bcc"] = path
            
            message.attach(MIMEText(body, "plain"))
            content = message.as_string()
            text = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, 465, context=text) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, path, content)
            Mouth.speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
        except Exception as e:
            Mouth.speak("Đã xảy ra lỗi")
            print(e)
        finally:
            server.close()
    else:
        Mouth.speak('thiện tâm không hiểu bạn muốn gửi email cho ai')


def assistant():
    Mouth.speak("Trợ lý chân thiện tâm Xin chào, bạn tên là gì nhỉ?")
    # name = hieu.get_text()
    name='ánh'
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
            # elif "mở" in text:  
            #     open_application()
            # elif 'website' in text or 'lên mạng' in text:
            #     open_website()
            # elif "đóng" in text:
            #     close_application(text)

            elif "email" in text or "mail" in text or "gmail" in text:
                send_email(text)
            # elif "chơi nhạc" in text:
            #     play_song()
            # elif "hình nền" in text:
            #     change_wallpaper()
            # elif "đọc báo" in text:
            #     read_news()
            else:
                Mouth.speak(f"{name} cần thiện tâm giúp gì ạ?")

assistant()