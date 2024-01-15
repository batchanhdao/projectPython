# @title Văn bản tiêu đề mặc định
import requests # web: html + css
from bs4 import BeautifulSoup as bs
import random
import pandas as pd
from time import sleep
from selenium import webdriver # web: html + css + javasricpt
from selenium.webdriver.common.keys import Keys #Keys: cung cấp các phím trên bàn phím
from selenium.webdriver.common.by import By # By: định vị các thành phần trong tài liệu.
from selenium.webdriver.chrome.service import Service
import os
import urllib3 # download
from urllib.parse import urlparse, urljoin
import pyautogui as pag, sys # điều khiển bàn phím và chuột 
import pyperclip as ppc # copy/parse
import cv2
import wget
from webdriver_manager.chrome import ChromeDriverManager


# tạo thư mục làm việc
working_path=r"D:\anh\download\craw-data\phatphapungdung"
os.chdir(working_path)
print(os.getcwd())

# tìm page cơ sở, số trang từ 1-> đến, page_first, 
# page_coso = "https://phatphapungdung.com/sach-noi/hat-giong-tam-hon/page/" #2->18
page_coso = "https://phatphapungdung.com/sach-noi/truyen-lich-su-audio/page/" #2->18
page_links = list()
# page_first = "https://phatphapungdung.com/sach-noi/hat-giong-tam-hon"
page_first = "https://phatphapungdung.com/sach-noi/truyen-lich-su-audio"
page_links.append(page_first)
for page in range(2, 5):
   page_links.append(page_coso + str(page))

folder_image_path = 'image'
books_data = {'title': list(), 'link audio': list(), 'img url': list()}
tracks_data = {'title': list(), 'track': list(), 'link': list()}

def stop_next():
    print("Function stop_next running")
    while(True):
        sleep(0.5)
        key = input("Enter 'ok' to next: ").strip().lower()
        if key == "ok":
            print("Program is continuing")
            return
        
def sleepRandom(start=1, end=3, phay=2): # hàm random thời gian ngủ để qua khâu kiểm duyệt 
    # start/end: random time from start -> end 
    # phay: phần trăm của 1 số vd phay=2 -> 2.22
    phantram = 10**phay
    thoigian = random.randint(start*phantram, end*phantram)/phantram
    sleep(thoigian)

# hàm ghi file: đường dẫn, văn bản
def writeFileTxt(path_file, text, mode='w', encoding='UTF-8'):
  print('function: writeFileTxt running')
  # Check if the text is a set
  if isinstance(text, set):
    text = list(text)
  # Check if the text is a list/tuple.
  if isinstance(text, (list, tuple)):
    text = '\n'.join(text)
  with open(path_file, mode=mode, encoding=encoding) as file:
    file.write(text)
    # print("write text:", text)
  print('Finished function: writeFileTxt')



# hàm download file: # url / path to fordel -> mode = 1/file -> mode = 0
def downloadFile(url, path_file, mode=0):
  print('function: downloadFile running')
  response = requests.get(url) # send request to url and receive result
  if response.status_code == 200: # check status connection: 200 is OK
    if mode == 1:
      name_file = os.path.basename(urlparse(url).path)
      path_file = os.path.join(path_file, name_file)
    dir_name = os.path.dirname(path_file)
    if dir_name != "" and not os.path.exists(dir_name):
      os.makedirs(dir_name)
    with open(path_file, 'wb') as file: # write file jpg/png
        file.write(response.content)
    print(f"Downloaded: {url}")
  else:
    print(f"Failed to download: {url}")
  response.close()
  sleepRandom()
  print('Finished function: downloadFile')


# hàm download file Pro: # url / path to fordel -> mode = 1/file -> mode = 0: pdf/mp3/mp4
def downloadFilePro(url, path_file, mode=0):
  print('function: downloadFilePro running')
  try:
    if mode == 1:
      name_file = os.path.basename(urlparse(url).path)
      path_file = os.path.join(path_file, name_file)
    dir_name = os.path.dirname(path_file)
    if dir_name != "" and not os.path.exists(dir_name):
      os.makedirs(dir_name)
    wget.download(url, out=path_file)
    print(f"Downloaded: {url}")
  except Exception as e:
    print(f"Failed to download: {url}")
    print(e)
  sleepRandom()
  print('Finished function: downloadFilePro')

def craw_data_playlist(audiobooks, file_audio_path):
    print("Function craw_data_playlist running")
    text_list = list()
    for audio in audiobooks:
        books_data['title'].append(audio["title"])
        books_data['link audio'].append(audio["link audio"])
        books_data['img url'].append(audio["img url"])
        text = "++" + audio["title"] + "; " + audio["link audio"] + "; " + audio["img url"]
        text_list.append(text)
        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            link_audio = audio["link audio"]
            # print(link_audio)
            driver.get(link_audio)
            soup = bs(driver.page_source, 'html.parser')
            playlist = soup.find('div', {'class': 'fp-playlist-external is-audio fv-playlist-design-2017 visible-captions fp-playlist-horizontal fp-playlist-has-captions skin-youtuby'})
            a_elements = playlist.find_all('a', {'data-item': True})

            for a_element in a_elements:
                # Extract the 'data-item' attribute content as a string
                data_item_content = a_element['data-item']
                # Convert the 'data-item' content to a dictionary
                data_item_dict = eval(data_item_content)
                # Access the 'src' attribute inside the dictionary
                src_value = str(data_item_dict['sources'][0]['src']).replace('\\', '').strip()
                # name audio
                name = str(a_element.find('span').get_text()).strip()
                tracks_data['title'].append(audio["title"])
                tracks_data['track'].append(name)
                tracks_data['link'].append(src_value)
                text = "Track: " + name + "; " + "Link track: " + src_value
                text_list.append(text)
            
            sleepRandom()
        except Exception as e:
            print('Error:', audio)
            print(e)
            # stop_next()
        finally:
            driver.quit()
    writeFileTxt(file_audio_path, text_list)
    print('Finished function: craw_data_playlist')


def main(url, name_file):
    print('Function main running')
    print('url:', url)
    # thiết lập url và kiểm tra kết nối
    r = requests.get(url) # # Send an HTTP request to the URL and lấy data chưa qua xử lý
    if r.status_code == 200:
        try:
          file_audio_path = name_file
          audiobooks = list()
          # open it, go to a website, and get results
          wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
          wd.get(url) #điều hướng đến trang được cung cấp bởi URL.
          # định dạng và lấy data bằng thư viện BeautifulSoup
          html_doc = wd.page_source
          soup = bs(html_doc, 'html.parser')

          # crawl data to div: main_content
          main_content = soup.find('div', {'class': 'td-pb-span8 td-main-content'})
          # print('main_content: ', main_content)

          a_tabs = main_content.find_all('a', {'class': 'td-image-wrap'}) # get list all <a> to source
          for a in a_tabs:
              link_audio = str(a.get('href')).strip()
              title = str(a.get('title')).strip()
              if ',' in title:
                title.replace(',',' - ')
              img_url = str(a.find('img').get('data-img-url')).strip()
              audio = {"title":title, "link audio":link_audio, "img url":img_url}
              audiobooks.append(audio)

          craw_data_playlist(audiobooks, file_audio_path)
        except Exception as e:
          print('Error at url:', url)
          print(e)
        finally:
          wd.quit()

    else:
        print(f"Status url : {r.status_code}")
        print(f"Error url : {url}")
    sleepRandom()



  

# craw_data_playlist(audiobooks)
for page in range(0, len(page_links)):
    url = page_links[page]
    name_file = f'page{page+1}.txt'
    # print(url, name_file)
    main(url, name_file)

books_df = pd.DataFrame(books_data)
tracks_df = pd.DataFrame(tracks_data)
# Ghi vào file Excel
with pd.ExcelWriter('truyen-lich-su-audio.xlsx') as writer:
    books_df.to_excel(writer, sheet_name='Books', index=False)
    tracks_df.to_excel(writer, sheet_name='Tracks', index=False)






