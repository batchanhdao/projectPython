import cv2
import dlib
import time
import math
import numpy as np
import random
import face_recognition
import os

# Khởi tạo bộ phát hiện khuôn mặt và bộ xác thực điểm mốc
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
imgList = {}  # key and value
path = "./imagesDB"


def getImagesEncoded(path):
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


# hàm tính toán nhấp nháy mắt
def calculate_eyes_ratio(eye):
    result = (((abs(eye[1][0] - eye[5][0]) ** 2 + abs(eye[1][1] - eye[5][1]) ** 2) ** 0.5) +
              ((abs(eye[2][0] - eye[4][0]) ** 2 + abs(eye[2][1] - eye[4][1]) ** 2) ** 0.5)) / (2 * (
        ((abs(eye[0][0] - eye[3][0]) ** 2 + abs(eye[0][1] - eye[3][1]) ** 2) ** 0.5)))
    return result


def calculate_mouth_ratio(mouth):
    result = ((abs(mouth[14][0] - mouth[18][0]) ** 2 + abs(mouth[14][1] - mouth[18][1]) ** 2) ** 0.5)
    return result


def draw_points(points, image, color):
    # Vẽ các điểm mốc trên khuôn mặt
    for point in points:
        # cv2.circle(hình ảnh, tọa độ trung tâm, bán kính, màu sắc, độ dày)
        cv2.circle(image, (point[0], point[1]), 2, color, -1)


# Hàm để vẽ hình chữ nhật và điểm mốc trên khuôn mặt
def draw_landmarks(image, landmarks, rectangle):
    # Vẽ hình chữ nhật quanh khuôn mặt
    cv2.rectangle(image, (rectangle.left(), rectangle.top()), (rectangle.right(), rectangle.bottom()), (0, 255, 0), 2)

    # Vẽ các điểm mốc trên khuôn mặt
    draw_points(landmarks, image, (0, 0, 255))


# Hàm để kiểm tra người dùng đã nhắm mắt hay chưa
def check_blinking(landmarks, image, beside):
    T = 0.2
    # Lấy tọa độ của mắt trái và mắt phải
    right_eye = landmarks[36:42]
    left_eye = landmarks[42:48]
    print("eye:")
    print(right_eye)
    print(left_eye)

    # Vẽ các điểm mốc trên left/right eye
    draw_points(right_eye, image, (255, 0, 0))
    draw_points(left_eye, image, (255, 0, 0))

    # Tính toán tỷ lệ mắt nhắm
    right_eye_aspect_ratio = calculate_eyes_ratio(right_eye)
    left_eye_aspect_ratio = calculate_eyes_ratio(left_eye)

    print("ty le nham mat")
    print(right_eye_aspect_ratio)
    print(left_eye_aspect_ratio)
    eyes = (left_eye_aspect_ratio + right_eye_aspect_ratio) / 2
    print("eyes", eyes)

    if beside == "left":
        # Trả về True nếu người dùng đã nhắm mắt trái
        return left_eye_aspect_ratio < T < right_eye_aspect_ratio
    elif beside == "right":
        # Trả về True nếu người dùng đã nhắm mắt phải
        return right_eye_aspect_ratio < T < left_eye_aspect_ratio
    else:
        # Trả về True nếu người dùng đã nhắm mắt
        return round(eyes, 2) < T


# hàm kiểm tra người dùng mở miệng trong 3s chưa
def open_mouth_for_a_few_seconds(landmarks, image, seconds):
    T = 10
    # Lấy tọa độ của miệng
    mouth = landmarks[48:68]

    # Vẽ các điểm mốc trên mouth
    draw_points(mouth, image, (255, 0, 0))

    for second in range(seconds * 3):
        # Tính toán tỷ lệ mở miệng
        mouth_aspect_ratio = calculate_mouth_ratio(mouth)
        if mouth_aspect_ratio <= T:
            return False
        time.sleep(0.3)

    return True


# Hàm để kiểm tra đóng mở miệng
def check_mouth(landmarks, image):
    T = 10
    # Lấy tọa độ của miệng
    mouth = landmarks[48:68]
    print("mouth")
    print(mouth)
    # Vẽ các điểm mốc trên mouth
    draw_points(mouth, image, (255, 0, 0))

    # Tính toán tỷ lệ mở miệng
    mouth_aspect_ratio = calculate_mouth_ratio(mouth)

    print("ty le mo mieng")
    print(mouth_aspect_ratio)
    # Trả về True nếu người dùng đã mở miệng
    return mouth_aspect_ratio > T


def identification(imgList, img_input_encode):
    msv = ""
    tyle = 1
    #  duyệt các ảnh của sv. j là msv
    for j in imgList.keys():
        if len(imgList[j]) == 0:
            continue
        #  img là data ảnh của mỗi sv
        for img in imgList[j]:
            # so sánh khuôn mặt
            faceDis = face_recognition.face_distance(img, img_input_encode)
            matchIndex = np.argmin(faceDis)
            print("identification:", faceDis[matchIndex])
            if tyle > faceDis[matchIndex]:
                msv = str(j)
                tyle = faceDis[matchIndex]
    if tyle < 0.50:
        return msv
    else:
        return "unknow"


def is_one_face(past_face, present_face):
    faceDis = face_recognition.face_distance(past_face, present_face)
    matchIndex = np.argmin(faceDis)
    print("is one face:", faceDis[matchIndex])
    if faceDis[matchIndex] < 0.50:
        return True
    return False


# Hàm xác thực
def authentication(method_authentication):
    cap = cv2.VideoCapture(0)

    # t = random.randint(1, 3)
    t = 2
    print("time: ", t)
    blinking_eyes = 0
    open_mouth = 0
    close_left_eye = 0
    close_right_eye = 0
    past_eyes = True
    past_mouth = False
    time_no_have_face = 3
    past_face = []

    while True:
        poin_x, poin_y = 10, 30
        ret, frame = cap.read()
        try:
            # Chuyển đổi sang ảnh xám để tăng tốc độ xử lý
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Nhận diện khuôn mặt
            faces = detector(gray)
            # print("faces: ", len(faces))

            if method_authentication == 1:
                # kiểm tra có người xác thực không, nếu không có thì sau 3s sẽ xác thực lại
                if len(faces) == 0:
                    cv2.putText(frame, "no face", (poin_x, poin_y), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (0, 0, 255), 2)
                    poin_y += 40
                    if time_no_have_face:
                        blinking_eyes = 0
                        time_no_have_face -= 1
                        time.sleep(1)
                    else:
                        cv2.putText(frame, "re-authenticate", (poin_x, poin_y), cv2.FONT_HERSHEY_COMPLEX, 1,
                                    (0, 0, 255), 2)
                else:
                    image_input_encode = face_recognition.face_encodings(frame)[0]
                    if not past_face:
                        past_face.append(image_input_encode)

                    time_no_have_face = 3

                    face = faces[0]
                    # Dự đoán các điểm mốc trên khuôn mặt
                    landmarks = predictor(gray, face)
                    landmarks = [(landmark.x, landmark.y) for landmark in landmarks.parts()]

                    # Vẽ hình chữ nhật và điểm mốc trên khuôn mặt
                    draw_landmarks(frame, landmarks, face)

                    # kiểm tra người xác thực hiện tại và lúc trước có là 1 không, nếu không thì xác thực lại
                    if not is_one_face(past_face, image_input_encode):
                        blinking_eyes = 0
                        past_face.clear()
                        past_face.append(image_input_encode)

                    cv2.putText(frame, f"blinking eyes: {blinking_eyes}/{t}", (poin_x, poin_y),
                                cv2.FONT_HERSHEY_COMPLEX,
                                1, (0, 0, 255), 2)

                    if blinking_eyes == t:
                        break
                    # Xác thực
                    else:
                        present_eyes = check_blinking(landmarks, frame, "both")
                        # present_mouth = check_mouth(landmarks, frame)
                        # open/close eyes
                        if blinking_eyes != t and present_eyes != past_eyes:
                            past_eyes = present_eyes
                            if past_eyes:
                                blinking_eyes += 1
                            print("Blinking detected!", blinking_eyes)

            elif method_authentication == 2:
                # kiểm tra có người xác thực không, nếu không có thì sau 3s sẽ xác thực lại
                if len(faces) == 0:
                    cv2.putText(frame, "no face", (poin_x, poin_y), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (0, 0, 255), 2)
                    poin_y += 40
                    if time_no_have_face:
                        open_mouth = 0
                        time_no_have_face -= 1
                        time.sleep(1)
                    else:
                        cv2.putText(frame, "re-authenticate", (poin_x, poin_y), cv2.FONT_HERSHEY_COMPLEX, 1,
                                    (0, 0, 255), 2)
                else:
                    image_input_encode = face_recognition.face_encodings(frame)[0]
                    if not past_face:
                        past_face.append(image_input_encode)

                    time_no_have_face = 3

                    face = faces[0]
                    # Dự đoán các điểm mốc trên khuôn mặt
                    landmarks = predictor(gray, face)
                    landmarks = [(landmark.x, landmark.y) for landmark in landmarks.parts()]

                    # Vẽ hình chữ nhật và điểm mốc trên khuôn mặt
                    draw_landmarks(frame, landmarks, face)

                    # kiểm tra người xác thực hiện tại và lúc trước có là 1 không, nếu không thì xác thực lại
                    if not is_one_face(past_face, image_input_encode):
                        open_mouth = 0
                        past_face.clear()
                        past_face.append(image_input_encode)

                    cv2.putText(frame, f"open mouth: {open_mouth}/{t}", (poin_x, poin_y), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (0, 0, 255), 2)

                    if open_mouth == t:
                        break
                    # Xác thực
                    else:
                        # present_eyes = check_blinking(landmarks, frame, "both")
                        present_mouth = check_mouth(landmarks, frame)
                        # open/close mouth
                        if open_mouth != t and present_mouth != past_mouth:
                            past_mouth = present_mouth
                            if not past_mouth:
                                open_mouth += 1
                            print("Smile detected!", open_mouth)

            elif method_authentication == 3:
                # kiểm tra có người xác thực không, nếu không có thì sau 3s sẽ xác thực lại
                if len(faces) == 0:
                    cv2.putText(frame, "no face", (poin_x, poin_y), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (0, 0, 255), 2)
                    poin_y += 40
                    if time_no_have_face:
                        close_left_eye = 0
                        time_no_have_face -= 1
                        time.sleep(1)
                    else:
                        cv2.putText(frame, "re-authenticate", (poin_x, poin_y), cv2.FONT_HERSHEY_COMPLEX, 1,
                                    (0, 0, 255), 2)
                else:
                    image_input_encode = face_recognition.face_encodings(frame)[0]
                    if not past_face:
                        past_face.append(image_input_encode)
                    time_no_have_face = 3

                    face = faces[0]
                    # Dự đoán các điểm mốc trên khuôn mặt
                    landmarks = predictor(gray, face)
                    landmarks = [(landmark.x, landmark.y) for landmark in landmarks.parts()]

                    # Vẽ hình chữ nhật và điểm mốc trên khuôn mặt
                    draw_landmarks(frame, landmarks, face)

                    # kiểm tra người xác thực hiện tại và lúc trước có là 1 không, nếu không thì xác thực lại
                    if not is_one_face(past_face, image_input_encode):
                        close_left_eye = 0
                        past_face.clear()
                        past_face.append(image_input_encode)

                    cv2.putText(frame, f"close left eye: {close_left_eye}/{t}", (poin_x, poin_y), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (0, 0, 255), 2)
                    poin_y += 40

                    if close_left_eye == t:
                        break
                    elif check_blinking(landmarks, frame, "left"):
                        close_left_eye += 1
                        print("closed left eye")

            elif method_authentication == 4:
                # kiểm tra có người xác thực không, nếu không có thì sau 3s sẽ xác thực lại
                if len(faces) == 0:
                    cv2.putText(frame, "no face", (poin_x, poin_y), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (0, 0, 255), 2)
                    poin_y += 40
                    if time_no_have_face:
                        close_right_eye = 0
                        time_no_have_face -= 1
                        time.sleep(1)
                    else:
                        cv2.putText(frame, "re-authenticate", (poin_x, poin_y), cv2.FONT_HERSHEY_COMPLEX, 1,
                                    (0, 0, 255), 2)
                else:
                    image_input_encode = face_recognition.face_encodings(frame)[0]
                    if not past_face:
                        past_face.append(image_input_encode)
                    time_no_have_face = 3

                    face = faces[0]
                    # Dự đoán các điểm mốc trên khuôn mặt
                    landmarks = predictor(gray, face)
                    landmarks = [(landmark.x, landmark.y) for landmark in landmarks.parts()]

                    # Vẽ hình chữ nhật và điểm mốc trên khuôn mặt
                    draw_landmarks(frame, landmarks, face)

                    # kiểm tra người xác thực hiện tại và lúc trước có là 1 không, nếu không thì xác thực lại
                    if not is_one_face(past_face, image_input_encode):
                        close_right_eye = 0
                        past_face.clear()
                        past_face.append(image_input_encode)

                    cv2.putText(frame, f"close right eye: {close_right_eye}/{t}", (poin_x, poin_y),
                                cv2.FONT_HERSHEY_COMPLEX, 1,
                                (0, 0, 255), 2)
                    poin_y += 40

                    if close_right_eye == t:
                        break
                    elif check_blinking(landmarks, frame, "right"):
                        close_right_eye += 1
                        print("closed right eye")
                        break

            elif method_authentication == 5:
                time_open_mouth = 3
                # kiểm tra có người xác thực không, nếu không có thì sau 3s sẽ xác thực lại
                if len(faces) == 0:
                    cv2.putText(frame, "no face", (poin_x, poin_y), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (0, 0, 255), 2)
                else:
                    image_input_encode = face_recognition.face_encodings(frame)[0]
                    if not past_face:
                        past_face.append(image_input_encode)

                    face = faces[0]
                    # Dự đoán các điểm mốc trên khuôn mặt
                    landmarks = predictor(gray, face)
                    landmarks = [(landmark.x, landmark.y) for landmark in landmarks.parts()]

                    # Vẽ hình chữ nhật và điểm mốc trên khuôn mặt
                    draw_landmarks(frame, landmarks, face)

                    # kiểm tra người xác thực hiện tại và lúc trước có là 1 không, nếu không thì xác thực lại
                    if not is_one_face(past_face, image_input_encode):
                        past_face.clear()
                        past_face.append(image_input_encode)

                    cv2.putText(frame, f"Open mouth for about {time_open_mouth} seconds", (poin_x, poin_y),
                                cv2.FONT_HERSHEY_COMPLEX, 1,
                                (0, 0, 255), 2)

                    if open_mouth_for_a_few_seconds(landmarks, frame, time_open_mouth):
                        print(f"finished open mouth for about {time_open_mouth} seconds")
                        break

        except Exception as e:
            print(e)

        finally:
            cv2.imshow("Frame", frame)
            time.sleep(0.01)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# hàm chính
def main():
    global imgList
    imgList = getImagesEncoded(path)
    # print(imgList)
    TIMES_CHECK = 3
    # xác thực
    for T in range(TIMES_CHECK):
        method_authentication = random.randint(1, 5)
        # 1: check_blinking(both), 2: check_mouth, 3: check_blinking(left), 4: check_blinking(right), 5: open_mouth(3s)
        authentication(method_authentication)

    # Xác thực thành công thì nhận dạng đó là ai

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        # Chuyển đổi sang ảnh xám để tăng tốc độ xử lý
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        try:
            # Nhận diện khuôn mặt
            faces = detector(gray)
            face = faces[0]

            # Vẽ hình chữ nhật quanh khuôn mặt
            cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0),
                          2)
            image_input_encode = face_recognition.face_encodings(frame)[0]
            msv = identification(imgList, image_input_encode)
            cv2.putText(frame, f"authenticated: {msv}", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (0, 0, 255), 2)
        except Exception as e:
            print(e)

        finally:
            cv2.imshow("Frame", frame)
            time.sleep(0.01)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
