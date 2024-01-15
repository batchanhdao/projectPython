import webbrowser as web
import pyautogui as pag, sys
import time
import cv2
import pyperclip as ppc


def XuLyNguoiNhan(ima,context,image):
    try:
        if "nhan_tin" in image: 
            loca = pag.locateOnScreen(ima,confidence=0.7)
            if loca:
                pag.click(loca)
                ppc.copy(context)
                time.sleep(3)
                pag.hotkey('ctrl','v')
                time.sleep(3)
                pag.press('enter')
            else:
                print("ERROR nhan tin")
                return 0
        elif "close_chat" in image:
            loca = pag.locateOnScreen(ima,confidence=0.7)
            if loca:
                pag.click(loca)
                time.sleep(3)
                pag.hotkey("ctrl","w")
            else:
                print("ERROR exit")
                return 0
        # else:
        #     loca = pag.locateOnScreen(ima,confidence=0.7)
        #     pag.click(loca)
        
    except Exception as e:
        print(e)
        return 0
    return 1

def Send(url,nguoi_nhan,content):
    # print(url)
    # print(nguoi_nhan)
    print(content)
    try:
        web.open(url)
        time.sleep(6)
        gui_tin = ["button_nhan_tin.png","close_chat.png"]
        for image in gui_tin:
            img = cv2.imread(r"D:\\hinh anh\\image_facebook"+"\\"+"\\"+image)
            pag.moveTo(1117,352)
            time.sleep(3)
            for j in range(3):
                kt = XuLyNguoiNhan(img,content,image)
                if kt:
                    print(f'search {image} success')
                    break
                if j==2:
                    return
        print(f'send messenge for {nguoi_nhan} success')

    except Exception as e:
        print(e)

def GiaDinh(nguoi_nhan, path):
    content=''
    name=str(nguoi_nhan).lower()
    if "bố" in name or "mẹ" in name:
        content=f"""Happy New Year \nTân xuân rộn ràng, trăm hoa đua nở. Con chúc {nguoi_nhan} năm mới an nhiên vui vẻ, tâm trí hài hòa \nHiểu thương dẫn lối trên biển trời mênh mông, dù sóng gió nổi lên, bên trong hay bên ngoài, bình tâm ta cùng bước ạ."""
    elif "cô" in name or "dì" in name or "chú" in name or "bác" in name or "cậu" in name or "mợ" in name:
        content=f"Happy New Year \nNăm mới cháu Ánh xin kính chúc {nguoi_nhan} \nCung chúc tân xuân phước vĩnh cửu \nChúc trong gia quyến được an khương \nTân niên lai đáo đa phú quý \nXuân đến an khương vạn thọ tường."
    elif "ông" in name or "bà" in name:
        content = f"Happy New Year \nNăm mới cháu Ánh xin kính chúc {nguoi_nhan} sống lâu, sống thọ, ngày nào cũng thật ý nghĩa và an vui ạ."
    elif "anh" in name or "chị" in name or "em" in name:
        if "em" in name:
            name1 = str(nguoi_nhan).replace("Em","").strip()
            content = f"Happy New Year \nNăm mới xin kính chúc {name1} một năm tràn đầy niềm vui và hạnh phúc: \nVui trong sức khoẻ, trẻ trong tâm hồn, khôn trong lý tưởng và trưởng thành mọi lĩnh vực."
        else:
            content = f"Happy New Year \nNăm mới xin kính chúc {nguoi_nhan} một năm tràn đầy niềm vui và hạnh phúc: \nVui trong sức khoẻ, trẻ trong tâm hồn, khôn trong lý tưởng và trưởng thành mọi lĩnh vực."
    Send(path,nguoi_nhan,content)

def Ban(nguoi_nhan, path):
    # content=f"Happy New Year \nNăm mới chúc {nguoi_nhan} gặp được nhiều thầy hiền trí, thêm được nhiều bạn tốt, đọc được nhiều sách hay."
    content = f"""Happy New Year
Ngày xuân chúc {nguoi_nhan} tươi vui
Trui rèn nội lực bên trong chính mình
Trước nuôi nội tại an bình
Sau mang tâm thiện, trí minh giúp người
Gieo yêu thương, gặt nụ cười
Gia đình vinh hiển, rạng ngời xuân tươi."""
    Send(path,nguoi_nhan,content)

def XuLy(key):
    dem=0
    while(dem<60):
        time.sleep(1)
        global data
        nguoi_nhan = data.readline().strip("\n").strip()
        if "<end>" in nguoi_nhan:
            return dem
        path = data.readline().strip("\n").strip()
        dem+=1
        if key == "gia đình":
            GiaDinh(nguoi_nhan,path)
        elif key == "bạn":
            Ban(nguoi_nhan,path)
        print(nguoi_nhan)
        print(path)
        print("-----------------------------------")
    return dem


with open("D:\\tai lieu\\DS_nguoi_nhan.txt",'r',encoding="utf-8") as data:
    gia_dinh=0; ban=0
    while(True):
        line = data.readline().strip("\n")
        if line=='':
            break
        elif "<gia đình>" in line:
            gia_dinh=XuLy("gia đình")
        elif "<bạn>" in line:
            ban=XuLy("bạn")
        else: continue
    print(gia_dinh)
    print(ban)

# web.open("http://www.facebook.com")   
# time.sleep(5)        

time.sleep(5)
pag.hotkey('alt', 'tab')   
