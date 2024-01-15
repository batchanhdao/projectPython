import Noi_speak as noi
from datetime import datetime
import Ket_thuc as kt

assistand_brain = ""
thu = {"Monday":"Thứ 2","Tuesday":"Thứ 3","Wednesday":"Thứ 4",
       "Thursday":"Thứ 5","Friday":"Thứ 6","Saturday":"Thứ 7","Sunday":"Chủ nhật"}
thang = {"January":"tháng 1","February":"tháng 2","March":"tháng 3","April":"tháng 4",
         "May":"tháng 5","June":"tháng 6","July":"tháng 7","August":"tháng 8",
         "September":"tháng 9","October":"tháng 10","November":"tháng 11","December":"tháng 12"}
buoi = {"AM":"sáng","PM":"chiều"}


def HieuEnglish(you_speech,language,voice):
    if you_speech == "":
        assistand_brain = "I can't hear you, try again"
    elif "hi" in you_speech or "hello" in you_speech :
        assistand_brain = "Hello admin! How are you."
    elif "today" in you_speech or "time" in you_speech:
        time = datetime.today()
        assistand_brain = time.strftime("%A, %d, %B, %Y, %p, %H hours %M minutes %S seconds")
    elif kt.KetThuc(you_speech):
        assistand_brain = "good bye admin! see you"
    else:
        assistand_brain = "I'm fine!"
    print(assistand_brain)
    assistand_brain = str(assistand_brain).lower()
    noi.Noi(assistand_brain,language,voice)

def HieuVi(you_speech,language,voice):
    if you_speech == "":
         assistand_brain = "tôi không thể nghe thấy bạn! Thử lại nhé"
    elif "chào" in you_speech or "xin chào" in you_speech:
        assistand_brain = "xin chào quản trị viên! Bạn khỏe không."
    elif "hôm nay" in you_speech or "thời gian" in you_speech:
        time = datetime.today()
        assistand_brain = time.strftime("%A %d %B %Y %p %H %M %S")
        thoigian = [str(x) for x in str(assistand_brain).split()]
        assistand_brain = str(thu.get(thoigian[0]) + " ngày " + thoigian[1] +" "+
        thang.get(thoigian[2]) + " năm " + thoigian[3] +" "+ buoi.get(thoigian[4]) +" "+
        thoigian[5] + " giờ " + thoigian[6] + " phút " + thoigian[7] + " giây")
    elif kt.KetThuc(you_speech):
        assistand_brain = "tạm biệt quản trị viên! Hẹn gặp lại"
    else:
        assistand_brain = "tôi ổn!"
    print(assistand_brain)
    assistand_brain = str(assistand_brain).lower()
    noi.Noi(assistand_brain,language,voice)

    # return assistand_brain
# noi.Noi(Hieu('what is today'))

def Hieu(you_speech,language,voice):
    if language == "vi":
        HieuVi(you_speech,language,voice)
    else :
        HieuEnglish(you_speech,language,voice)


"""HieuEnglish("i am anh","en",2)
HieuEnglish("time","en",2)
HieuEnglish("end","en",2)

HieuVi("toi la anh","vi",1)
HieuVi("hôm nay","vi",1)
HieuVi("dừng lai","vi",1)"""
