import os
import playsound
import speech_recognition as sr
# import sys
# import ctypes
# import wikipedia
# import datetime
import time
# import json
# import re
# import webbrowser
# import smtplib
# import requests
# import urllib
# import urllib.request as urllib2
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# from time import strftime
# from gtts import gTTS
# from youtube_search import YoutubeSearch
import Mouth
import Ears
import Stop

def get_text():
    # for i in range(20):
    #     text = Ears.listen_audio()
    #     if text:
    #         return text.lower()
    # Stop.stop()
    text = Ears.listen_audio()
    if text:
        return text.lower()
    return 0
