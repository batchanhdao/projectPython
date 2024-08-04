import requests # web: html + css
from bs4 import BeautifulSoup as bs
import random
import pandas as pd
from time import sleep
from selenium import webdriver # web: html + css + javasricpt
from selenium.webdriver.common.keys import Keys #Keys: cung cấp các phím trên bàn phím
from selenium.webdriver.common.by import By # By: định vị các thành phần trong tài liệu.
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import urllib3 # download
from urllib.parse import urlparse, urljoin
import pyautogui as pag, sys # điều khiển bàn phím và chuột 
import pyperclip as ppc # copy/parse
import cv2
import wget
from abc import ABC, abstractmethod
import json


class StopNext:
    def __init__(self):
        pass

    @staticmethod
    def stop_next():
        print("Function stop_next running")
        while(True):
            key = input("Enter 'ok' to next: ").strip().lower()
            if key == "ok":
                print("Program is continuing")
                return

    @staticmethod
    def sleep_random(start=1, end=4, phay=2): # hàm random thời gian ngủ để qua khâu kiểm duyệt
        # start/end: random time from start -> end
        # phay: phần trăm của 1 số vd phay=2 -> 2.22
        phantram = 10**phay
        thoigian = random.randint(start*phantram, end*phantram)/phantram
        sleep(thoigian)

class File(ABC):
    def __init__(self, path_file):
        self.path_file = path_file

    @abstractmethod
    def write_file(self, data, mode='w', encoding='UTF-8'):
        pass

class WriteTextIntoFileTxt(File):
    def __init__(self, path_file):
        super().__init__(path_file)

    def write_file(self, data, mode='w', encoding='UTF-8'):
        print('function: writeFileTxt running')
        with open(self.path_file, mode, encoding=encoding) as file:
            file.write(data)

class WriteListIntoFileTxt(File):
    def __init__(self, path_file):
        super().__init__(path_file)

    def write_file(self, data, mode='w', encoding='UTF-8'):
        print('function: writeFileTxt running')
        data = '\n'.join(data)
        with open(self.path_file, mode, encoding=encoding) as file:
            file.write(data)

class DownloadFile(ABC):
    def __init__(self, url, path_folder_save_files):
        # url: link download
        # path_save_files: path to save file
        self.url = str(url).replace('\\', '')
        self.path_folder_save_files = self.check_path(path_folder_save_files)
        self.name_file = self.get_name_file()

    def get_name_file(self):
        name_file = os.path.basename(urlparse(self.url).path)
        return name_file

    def check_path(self, path_folder_save_files):
        if not os.path.exists(path_folder_save_files):
            os.makedirs(path_folder_save_files)
        return path_folder_save_files

    @abstractmethod
    def download_file(self):
        pass

class DownloadFileByWget(DownloadFile):
    def __init__(self, url, path_folder_save_files):
        super().__init__(url, path_folder_save_files)

    def download_file(self):
      try:
        path_save_file = os.path.join(self.path_folder_save_files, self.name_file)
        wget.download(self.url, path_save_file)
        print()
        print(f"Downloaded: {path_save_file}")
      except Exception as e:
        print(e)
      StopNext().sleep_random()

class DownloadFileByRequest(DownloadFile):
    def __init__(self, url, path_folder_save_files):
        super().__init__(url, path_folder_save_files)

    def download_file(self):
      try:
        response = requests.get(self.url)
        if response.status_code == 200:
            path_save_file = os.path.join(self.path_folder_save_files, self.name_file)
            with open(path_save_file, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {path_save_file}")
        else:
            print(f"Failed to download: {self.url}")
        response.close()
      except Exception as e:
        print(e)
      StopNext().sleep_random()

if __name__ == "__main__":
    # tạo thư mục làm việc
    working_path=r"D:\anh\download\craw-data\phatphapungdung"
    os.chdir(working_path)
    print('Working path:', os.getcwd())

    # Khởi tạo đối tượng Service với ChromeDriverManager
    service = Service(ChromeDriverManager().install())

    page_links = [
        # 'https://phatphapungdung.com/sach-noi/trang-nguyen-viet-nam-3-178484.html',
        'https://phatphapungdung.com/the-buddha-cuoc-doi-duc-phat-121939.html',

    ]
    for page_link in page_links:
        try: 
            # Khởi tạo trình điều khiển Chrome với Service
            wd = webdriver.Chrome(service=service)
            wd.get(page_link)
            html_doc = wd.page_source
            soup = bs(html_doc, 'html.parser')
            # get title, url audio
            content = soup.find('div', {'class': 'td-post-content'})
            # print(len(content)) - 1
            try:
                title = content.find('h2').get_text()
            except:
                title = page_link.split('/')[-1].split('.')[0]
            # informations = content.find('p').get_text()

            # path_audiobooks = content.find('div', {'class': 'fp-playlist-external is-audio fv-playlist-design-2017 visible-captions fp-playlist-horizontal fp-playlist-has-captions skin-youtuby'})
            path_audiobooks = content.find('div', {'class': 'fp-playlist-external fp-playlist-vertical fp-playlist-only-captions skin-youtuby'})
            path_audiobooks = path_audiobooks('a')
            # print('Title:', title)
            # print('Informations:', informations)
            # print('Path audiobooks:', path_audiobooks)
            # print(len(path_audiobooks))

            for audiobook in path_audiobooks:
                path_audiobook = audiobook.get('data-item')
                path_audiobook = json.loads(path_audiobook)
                path_audiobook = path_audiobook['sources'][0]['src']
                # print(path_audiobook)
                downloadFileOb = DownloadFileByWget(url=path_audiobook, path_folder_save_files=os.path.join(working_path, title))
                downloadFileOb.download_file()
                # print(path_audiobook)
        except Exception as e:
            print('Error:', page_link)
            print(e)
        finally:
            wd.quit()
            StopNext().sleep_random()
    




