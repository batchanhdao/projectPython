from pydub import AudioSegment
import os

path_to_dir = r"D:\music" 
os.chdir(path_to_dir)
print(os.getcwd())

mp3_file_path = r"Hay-Yeu-Nhau-Di-Tran-Thu-Ha.mp3"
wav_file_path = r"test"

audio = AudioSegment.from_mp3(mp3_file_path)
print(len(audio))
step = 2*1000 # cắt video trong 2 giây 
for s in range(0, len(audio), step):
    try:
        # path đến file
        path_audio = os.path.join(wav_file_path, f'Hay-Yeu-Nhau-Di-Tran-Thu-Ha-{str(s)}.wav')
        os.path.normpath(path_audio)
        # print(s)
        # kiểm tra độ dài của s 
        if s+step > len(audio):
            wav = audio[s:len(audio)]
        else:
            wav = audio[s:s+step]
        # kiểm tra thư mục và file đã tồn tại chưa
        if os.path.exists(path_audio):
            wav.export(path_audio, format="wav")
        else:
            os.makedirs(os.path.dirname(path_audio), exist_ok=True)
            wav.export(path_audio, format="wav")
    except Exception as e:
        print(e)

# audio = audio[30*1000: 50*1000]
# audio.export(wav_file_path, format="wav")
