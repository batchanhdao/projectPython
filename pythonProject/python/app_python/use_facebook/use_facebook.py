import webbrowser as web
import pyautogui as pag, sys
import time
import cv2
import pyperclip as ppc
time.sleep(10)
def test_pyautogui():
    time.sleep(5)
    # point = pag.position()
    # print(point)
    pag.moveTo(1117,352)
    time.sleep(5)
    pag.hotkey("alt","tab")
    # pag.move(point)
    # toa_do = [[82,464],[225,717],[226,370]]
    # pag.click(x=point[0],y=point[1])
    # print(pag.size())
    # pag.click(x=541,y=555,clicks=2)
    # pag.scroll(30)
    # pag.click(x=541,y=555,button='right')


def XuLyNguoiNhan(ima,context,image):
    try:
        if "nhan_tin" in image: 
            loca = pag.locateOnScreen(ima,confidence=0.7)
            pag.click(loca)
            time.sleep(5)
            ppc.copy(context)
            pag.hotkey('ctrl','v')
            time.sleep(3)
            pag.press('enter')
        elif "close_chat" in image:
            loca = pag.locateOnScreen(ima,confidence=0.7)
            pag.click(loca)
            time.sleep(5)
            pag.hotkey("alt","left") # button back on google
        else:
            loca = pag.locateOnScreen(ima,confidence=0.7)
            pag.click(loca)
        return 1
    except Exception as e:
        print('e')
        return 0

def XuLyDuongDi(ima):
    try:
        loca = pag.locateOnScreen(ima,confidence=0.7)
        pag.click(loca)
        return 1
    except Exception as e:
        print(e)
        return 0

def use_facebook():
    ds_nguoi_nhan = {"phương":"sister.png","tôi":"me.png"}
    duong_di = ["ban_be.png","danh_sach_tuy_chinh.png","nhom_gia_dinh.png"]
    try:
        url = "http://www.facebook.com"
        web.open(url)
        for image in duong_di:
            print(image)
            time.sleep(5)
            img = cv2.imread(r"D:\\hinh anh\\image_facebook"+"\\"+"\\"+image)
            for j in range(3):
                kt = XuLyDuongDi(img)
                if kt:
                    print(f'search {image} success')
                    break
                if j==2:
                    return
        for nguoi_nhan, nhan_dang in ds_nguoi_nhan.items():
            gui_tin = [f"{nhan_dang}","button_nhan_tin.png","close_chat.png"]
            context = f"""{nguoi_nhan} ơi \nChúc 1 ngày an vui \nĐây là tin nhắn tự động \nxin đừng trả lời \nCảm ơn rất nhiều!"""
            for image in gui_tin:
                print(image)
                time.sleep(5)
                img = cv2.imread(r"D:\\hinh anh\\image_facebook"+"\\"+"\\"+image)
                for j in range(3):
                    kt = XuLyNguoiNhan(img,context,image)
                    if kt:
                        print(f'search {image} success')
                        break
                    if j==2:
                        return
            print(f'send messenge for {nguoi_nhan} success')

    except Exception as e:
        print(e)

# use_facebook()
# time.sleep(5)
# pag.hotkey('alt', 'tab')
test_pyautogui()

# >>> with pyautogui.hold('shift'):
#         pyautogui.press(['left', 'left', 'left'])
# >>> pyautogui.hotkey('ctrl', 'shift', 'esc')
# Point(x=29, y=78) | Point(x=80, y=78)