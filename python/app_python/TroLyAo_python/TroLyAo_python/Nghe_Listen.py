import speech_recognition as sr
import hieu_understand as hieu
import Noi_speak as noi
import Ket_thuc as kt

def NgheEnglish(language,voice):
    have_next = True
    while have_next:
        assistant_ear = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Assistant Listening")
            noi.Noi("Assistant Listening",language,voice)
            audio = assistant_ear.listen(mic)

        try:
            # you = assistant_ear.recognize_google(audio)
            you = assistant_ear.recognize_google(audio)
        except:
            you = ""
        print('You: ' + you)

        # noi.Noi(hieu.Hieu(str(you).lower()))
        hieu.Hieu(str(you).lower(),language,voice)
        # have_next=False

        end_listen = str(you).lower()
        if kt.KetThuc(end_listen):
            have_next = False

def NgheVi(language,voice):
    have_next = True
    while have_next:
        assistant_ear = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Trợ lý ảo đang nghe")
            noi.Noi("Trợ lý ảo đang nghe",language,voice)
            audio = assistant_ear.listen(mic)

        try:
            # you = assistant_ear.recognize_google(audio)
            you = assistant_ear.recognize_google(audio,language="vi-VN")
        except:
            you = ""
        print('Bạn: ' + you)

        # noi.Noi(hieu.Hieu(str(you).lower()))
        hieu.Hieu(str(you).lower(),language,voice)
        # have_next=False

        end_listen = str(you).lower()
        if "tạm biệt" in end_listen or "hẹn gặp lại" in end_listen or "an" in end_listen:
            have_next=False

def Nghe(language,voice):
    if language == "vi":
        NgheVi(language,voice)
    else:
        NgheEnglish(language,voice)





