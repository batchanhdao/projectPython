import os
import cv2
import face_recognition
import time


list_images = []
path = "D:/pythonProject_NhanDienKhuonMat/NhanDienKhuonMat_version2/static/imagesDB"
def DataSv(name, msv):
    for i in os.listdir(path):
        if i == msv:
            return
    os.mkdir(path+'/'+msv)
    # file_write = open("userDB.txt", "a", encoding="utf-8")
    # file_write.write(msv+'-'+name+'\n')
    # file_write.close()

def SaveImages(msv):
    global list_images
    i = 0
    for frame in list_images:
        cv2.imwrite(f"{path}/{msv}/{msv}_pic{i}.jpg", frame)
        i += 1
    list_images.clear()

def SetImages():
    global list_images
    list_images.clear()
    cap = cv2.VideoCapture(0)
    i=0
    while True:
        ret, frame = cap.read()
        img = frame
        if not ret:
            break
        person = len(face_recognition.face_locations(frame))
        if person==1:
            list_images.append(frame)
            i+=1
            local_faces_input = face_recognition.face_locations(frame)[0]
            # cv2.rectangle(img, (local_faces_input[3], local_faces_input[0]),
            #               (local_faces_input[1], local_faces_input[2]), (0, 0, 255), 2)
        if i>9:
            cv2.rectangle(img, (local_faces_input[3], local_faces_input[0]),
                          (local_faces_input[1], local_faces_input[2]), (0, 0, 255), 2)
            cv2.putText(img, "Finished", (local_faces_input[3], local_faces_input[2] + 27), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (0, 255, 0), 2)
        ret, buffer = cv2.imencode('.jpg', img)
        img_output = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img_output + b'\r\n')

        if i==10:
            break
        time.sleep(0.5)
        # cv2.imshow('anh', frame)
        # if cv2.waitKey(100) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
        #     break
    cap.release()  # giải phóng camera
    cv2.destroyAllWindows()  # thoát tất cả các cửa sổ
    # print(i)

def GetImages(msv):
    listImg = []
    for pic in os.listdir(f'{path}/{msv}'):
        img = str(f"{pic}")
        listImg.append(img)
    return listImg

def DeteleImage(name):
    try:
        os.remove(path+'/'+name)
        print(f"Xóa tập tin {path+'/'+name} thành công!")
    except OSError as e:
        print(f"Lỗi: {e.filename} - {e.strerror}.")
