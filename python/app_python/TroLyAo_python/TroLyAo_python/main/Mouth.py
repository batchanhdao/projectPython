import os
import playsound
import time
from gtts import gTTS

# wikipedia.set_lang('vi')
language = 'vi'

def speak(text):
    print("Trợ lý Chân Thiện Tâm: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("C:\\Users\\lea81\\Downloads\\TroLyAo_python\\lehonganh.mp3")
    playsound.playsound("C:\\Users\\lea81\\Downloads\\TroLyAo_python\\lehonganh.mp3", True)
    time.sleep(0.1)
    os.remove("C:\\Users\\lea81\\Downloads\\TroLyAo_python\\lehonganh.mp3")
    time.sleep(1.5)
