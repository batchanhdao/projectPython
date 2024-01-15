import webbrowser as web
import pyautogui as pgui, sys
import time
import cv2
import pyperclip as ppc

time.sleep(10)
def test_pyautogui():

    time.sleep(5)
    point = pgui.position()
    print(point)
    # toa_do = [[82,464],[225,717],[226,370]]
    # pgui.click(x=point[0],y=point[1])
    # print(pgui.size())
    # pgui.click(x=541,y=555,clicks=2)
    # pgui.scroll(30)
    # pgui.click(x=541,y=555,button='right')


def XuLyNguoiNhan(ima,context):
    try:
        loca = pgui.locateOnScreen(ima,confidence=0.7)
        pgui.click(loca)
        time.sleep(5)
        ppc.copy(context)
        pgui.hotkey('ctrl','v')
        time.sleep(3)
        pgui.press('enter')
        return 1
    except Exception as e:
        print('e')
        return 0

def XuLyDuongDi(ima,nguoi_nhan):
    try:
        loca = pgui.locateOnScreen(ima,confidence=0.7)
        pgui.click(loca)
        ppc.copy(nguoi_nhan)
        time.sleep(3)
        pgui.hotkey('ctrl','v')
        return 1
    except Exception as e:
        print(e)
        return 0
def DuongDi(duong_di,nguoi_nhan):
    for image in duong_di:
        print(image)
        time.sleep(5)
        img = cv2.imread(r"D:\\hinh anh\\image_zalo"+"\\"+"\\"+image)
        for j in range(3):
            kt = XuLyDuongDi(img,nguoi_nhan)
            if kt:
                print(f'search {image} success')
                break
            if j==2:
                return

def use_zalo():
    ds_nguoi_nhan = {"chị phương":"sister.png","bố cảnh":"father.png"}
    duong_di = ["search.png"]
    try:
        # mở zalo
        url = "https://chat.zalo.me/"
        web.open(url)
        time.sleep(5)
        # Tìm kiếm người nhận + gửi tin
        for nguoi_nhan, nhan_dang in ds_nguoi_nhan.items():
            gui_tin = [f"{nhan_dang}"]
            context = f"""{nguoi_nhan} ơi \nChúc 1 ngày an vui \nĐây là tin nhắn tự động \nxin đừng trả lời \nCảm ơn rất nhiều!"""
            DuongDi(duong_di,nguoi_nhan) # tìm kiếm người nhận
            # Xử lý gửi tin
            for image in gui_tin:
                print(image)
                time.sleep(5)
                img = cv2.imread(r"D:\\hinh anh\\image_zalo"+"\\"+"\\"+image)
                for j in range(3):
                    kt = XuLyNguoiNhan(img,context)
                    if kt:
                        print(f'send messenge for {nguoi_nhan} success')
                        break
                    if j==2:
                        return

    except Exception as e:
        print(e)

use_zalo()
time.sleep(5)
pgui.hotkey('alt', 'tab')
# test_pyautogui()
