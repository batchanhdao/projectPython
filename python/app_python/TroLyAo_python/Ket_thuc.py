
Ds=["bye", "tạm biệt", "see you", "hẹn gặp lại",
    "stop", "dừng", "end", "kết thúc"]
def KetThuc(you_speech):
    for text in Ds:
        if text in you_speech:
            return True
    return False
