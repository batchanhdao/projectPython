import os
import time
import subprocess
#----------------------------------------------
import Understand as hieu
import Mouth
import Stop

def open_application(text): #!!!
    try:
        if "google" in text:
            os.startfile(
                'C:\\Program Files\\Google\Chrome\\Application\\chrome.exe'
                # 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
                )
        elif "microsoft" in text:
            os.startfile(
                'C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge.exe'
                # 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
                )
        elif "word" in text or "soạn thảo" in text:
            os.startfile(
                # 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
                )
        elif "powerpoint" in text or "trang trình bày" in text:
            os.startfile(
                # 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
                )
        elif "excel" in text or "trang tính" in text:
            os.startfile(
                # 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
                )
        elif "outlook" in text :
            os.startfile(
                # 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE'
                )
        elif "access" in text :
            os.startfile(
                # 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSACCESS.EXE'
                )
        elif "điều khiển máy tính" in text :
            os.startfile(
                # 'C:\\Program Files (x86)\\UltraViewer\\UltraViewer_Desktop.exe'
                )
        elif "đọc pdf" in text :
            os.startfile(
                # 'C:\\Program Files (x86)\\Foxit Software\\Foxit Reader\\FoxitReader.exe'
                )
        elif "zoom" in text:
            os.startfile(
                # 'C:\\Users\\Admin\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
                )
        elif "gõ chữ" in text:
            os.startfile(
                # 'C:\\Program Files\\EVKey\\EVKey.exe'
                )
        elif "github" in text:
            os.startfile(
                # 'C:\\Users\\Admin\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe'
                )
        elif "máy ảo" in text:
            os.startfile(
                # 'C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe'
                )
        elif "sql" in text:
            os.startfile(
                # 'C:\\Program Files\\MySQL\\MySQL Workbench 8.0 CE\\MySQLWorkbench.exe'
                )
        elif "netbean" in text:
            os.startfile(
                # 'C:\\Program Files\\NetBeans-14\\netbeans\\bin\\netbeans64.exe'
                )
        elif "pycharm" in text:
            os.startfile(
                # 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.3\\bin\\pycharm64.exe'
                )
        elif "code" in text:
            os.startfile(
                # 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                )
        elif "notepad" in text:
            os.startfile(
                # 'C:\\Windows\\System32\\notepad.exe'
                )
        elif "ổ c" in text:
            os.startfile(
                'C:')
        elif "ổ d" in text:
            os.startfile(
                # 'D:'
                )
        elif "tài liệu" in text:
            os.startfile(
                'C:\\Users\\lea81\\Documents')
        elif "admin" in text:
            os.startfile(
                'C:\\Users\\Admin')
        elif "nhạc" in text:
            path='C:\\Users\\lea81\\Music'
            for file in os.listdir(path):
                if file.endswith('.mp3'):
                    print(file)
                    os.startfile(path+'\\'+file)
                    time.sleep(100)
                    # subprocess.call("TASKKILL /F /IM Music.UI.exe",shell=True)
        elif "ảnh" in text:
            path='C:\\Users\\lea81\\OneDrive\\Pictures'
            for file in os.listdir(path):
                if file.endswith('.png') or file.endswith('jpg'):
                    print(file)
                    os.startfile(path+'\\'+file)
                    time.sleep(10)
                    # subprocess.call("TASKKILL /F /IM Microsoft.Photos.exe",shell=True)
        else:
            return Mouth.speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
    except Exception as e:
        print(e)
        return Mouth.speak("đã xảy ra lỗi")
    return Mouth.speak(f"đã mở {text}")

def close_application(text):
    try:
        if "google" in text:
            subprocess.call("TASKKILL /F /IM chrome.exe",shell=True)
        elif "microsoft" in text:
            subprocess.call("TASKKILL /F /IM msedge.exe",shell=True)
        elif "nhạc" in text:
            subprocess.call("TASKKILL /F /IM Music.UI.exe",shell=True)
        elif "ảnh" in text:
            subprocess.call("TASKKILL /F /IM Microsoft.Photos.exe",shell=True)
        else:
            return Mouth.speak("Ứng dụng chưa được mở. Bạn hãy thử lại!")
    except Exception as e:
        print(e)
        return Mouth.speak("đã xảy ra lỗi")
    return Mouth.speak(f"đã {text}")