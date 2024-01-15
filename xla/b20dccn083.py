import numpy as np
import cv2

image = cv2.imread("D:\\hinh anh\\pexels-pixabay-210186.jpg")  # Đọc ảnh từ đường dẫn

# Hiển thị ảnh trong cửa sổ
def showImage():
    cv2.imshow('Image', image)

def imWrite():
    cv2.imwrite('output_image.jpg', image)

# Chuyển đổi ảnh màu thành ảnh xám:
def grayImage():
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    showImage()

# đọc dữ liệu video từ tệp hoặc thiết bị đầu vào
def readVideo():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if cv2.waitKey(1) == ord('q'):
            break
        cv2.imshow('image', frame)
    cap.release()
    cv2.destroyAllWindows()

# tạo và ghi dữ liệu video
# def writeVideo():

showImage()
readVideo()