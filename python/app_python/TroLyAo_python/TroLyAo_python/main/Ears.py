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

def listen_audio():
    assistant_ear = sr.Recognizer()
    with sr.Microphone() as source:
        print("Trợ lý ảo đang nghe")
        audio = assistant_ear.listen(source, phrase_time_limit=8)
        try:
            text = assistant_ear.recognize_google(audio, language="vi-VN")
            print("Bạn: "+text)
            return text
        except:
            print("...")
            return 0
