import speech_recognition as sr
import os
import fnmatch

def convert_mp3_to_text(mp3_file):
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(mp3_file) as source:
        audio = recognizer.record(source)

    try:
        # Use Google Speech Recognition
        # text = recognizer.recognize_google(audio, language="en-US")
        text = recognizer.recognize_google(audio, language="vi-VN")
        # ja - ko - fr-FR - vi-VN - zh-CN
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    return None

path_to_dir = r"D:\music\test"

# Lấy danh sách các file trong thư mục
files = os.listdir(path_to_dir)
# Sắp xếp danh sách file theo số nguyên trong tên file
sorted_files = sorted(files, key=lambda x: int(x.split('-')[-1].split('.')[0]))
# In ra danh sách đã sắp xếp
for file in sorted_files:
    path_to_file = os.path.join(path_to_dir, file)
    if os.path.isfile(path_to_file) and fnmatch.fnmatch(file, "*.wav"):
        print(file)
        # result_text = convert_mp3_to_text(path_to_file)
        # if result_text:
        #     print("Converted text:")
        #     print(result_text)
