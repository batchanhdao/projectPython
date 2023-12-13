import os
import numpy as np
import cv2
import face_recognition

class Picture:
    def __init__(self):
        pass
    # lấy và xử lý ảnh sinh viên trong hệ thống
    def getImagesEncoded(self, path):
        # save key: msv and value: image encoded
        # folder's name is msv
        imgList = {}
        try:
            for folder in os.listdir(path):
                # get path folder to list picture
                path_pic = os.path.join(path, folder)
                # get path list images
                list_pic = os.listdir(path_pic)
                imgData = []  # danh sách ảnh của 1 sinh viên đã đc mã hóa
                for pic in list_pic:
                    # read image
                    img = cv2.imread(f"{path_pic}/{pic}")
                    # encode image
                    encode = face_recognition.face_encodings(img)
                    imgData.append(encode)
                imgList[folder] = imgData
        except Exception as e:
            print(e)
        finally:
            return imgList