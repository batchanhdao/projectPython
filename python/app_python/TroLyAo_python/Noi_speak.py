import pyttsx3

troLy_assistant = pyttsx3.init()  # tạo đối tượng

def NoiEnglish(you_speech,voice):
    assistant_say = you_speech
    # print(gtts.lang.tts_langs())
    global troLy_assistant
    Speaking_speed(140) # tốc độ giọng nói mới 10-1000
    Volume(1.0) # mức âm lượng từ 0 đến 1
    Voices(voice) # 1 cho nữ, 0 cho nam
    # Save(assistant_say,"test.mp3")

    # dung ham say(x) de noi
    troLy_assistant.say(assistant_say)
    # troLy_assistant.say("xin chào quản trị viên")
    #---------------------------------------------
    try:
        troLy_assistant.runAndWait()
    except:
        print('error')

def NoiVi(you_speech,voice):
    assistant_say = you_speech
    # print(gtts.lang.tts_langs())
    global troLy_assistant
    Speaking_speed(150) # tốc độ giọng nói mới 10-1000
    Volume(1.0) # mức âm lượng từ 0 đến 1
    Voices(voice) # 1 cho nữ, 0 cho nam

    troLy_assistant.say(assistant_say)
    try:
        troLy_assistant.runAndWait()
    except:
        print('error')

""" Tốc độ nói """
def Speaking_speed(speed):
    speaking_speed = troLy_assistant.getProperty('rate')  # nhận thông tin chi tiết về tốc độ nói hiện tại
    # print(speaking_speed)  # in tốc độ giọng nói hiện tại
    troLy_assistant.setProperty('rate', speed)  # thiết lập tốc độ giọng nói mới

""" ÂM LƯỢNG """
def Volume(level):
    volume = troLy_assistant.getProperty('volume')  # tìm hiểu mức âm lượng hiện tại (min=0 và max=1)
    # print(volume)  # in mức âm lượng hiện tại
    troLy_assistant.setProperty('volume', level)  # thiết lập mức âm lượng từ 0 đến 1

""" Giọng nói """
def Voices(voice):
    voices = troLy_assistant.getProperty('voices')  # nhận thông tin chi tiết về giọng nói hiện tại
    # for v in voices:
    #     print(v)
    troLy_assistant.setProperty('voice', voices[voice].id)  # thay đổi chỉ mục, thay đổi giọng nói. 1 cho nữ, 0 cho nam

"""Lưu giọng nói vào tệp"""
def Save(string,ten):
    troLy_assistant.save_to_file('Xin chào thế giới', 'test.mp3')
    troLy_assistant.runAndWait()
# Noi("Nice to meet you! i am my assistand ")
# Noi("Trợ lý áo tiếng việt")

def Noi(you_speech,language,voice):
    if language == "vi" :
        NoiVi(you_speech,voice)
    else :
        NoiEnglish(you_speech,voice)