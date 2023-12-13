import numpy as np
import cv2
import face_recognition
import datetime
import os
import shutil

from flask import Response, redirect, url_for, json, session, Flask

from NhanDIenKhuonMat_version2.Service import SetPicture, model_check
from NhanDIenKhuonMat_version2.Service.PictureModel import Picture
from NhanDIenKhuonMat_version2.Entity.student import Students
from NhanDIenKhuonMat_version2.extension import db
from NhanDIenKhuonMat_version2.Service.DataSV import DataSV
from flask import Blueprint, render_template, request
from flask_sse import sse
cap = cv2.VideoCapture(0)

# create the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///xla.db"
# Tạo đối tượng SQLAlchemy
db.init_app(app)
app.config['REDIS_URL'] = 'redis://localhost'
app.register_blueprint(sse, url_prefix='/stream')
app.secret_key = 'anhgdt1710'


# danh sách mã sv
ds_msv = []
# ds sinh viên điểm danh
ds_check_sv = []
# thời gian
day = datetime.datetime.now().strftime("%d%m%Y")
# danh sach sv
ds_sv = list()

dataSV = DataSV()
pictureModel = Picture()

ds_msv = dataSV.getDsMSV(day)
print(f"msv day {day}: ")
print(ds_msv)

# danh sách ảnh trong imgDB đã đc mã hóa
imgList = {}  # key and value
path = "D:/pythonProject_NhanDienKhuonMat/NhanDienKhuonMat_version2/static/imagesDB"
imgList = pictureModel.getImagesEncoded(path)

# lưu sinh viên mới vào danh sách điểm danh and ds_msv
def SaveDB(msv, time):
    global ds_msv
    global ds_check_sv
    try:
        file_write = open(f"D:/pythonProject_NhanDienKhuonMat/NhanDienKhuonMat_version2/diemdanh{day}.txt", "a", encoding="utf-8")
        for student in Students:
            if msv == student.getMsv():
                file_write.write(student.getMsv() + "-" + student.getFullname() + "-" + str(time).split()[1] + '\n')
                ds = {}
                ds['msv'] = student.getMsv()
                ds['name'] = student.getFullname()
                ds['time'] = str(time).split()[1]
                ds_check_sv.append(ds)
                ds_msv.append(msv)
                break
            else:
                continue
    except Exception as e:
        print(e)
    finally:
        file_write.close()


# hàm nhận dạng sinh viên
# data ảnh - ảnh cần check - vị trí mặt trong ảnh check - ảnh input
def NhanDang(imgList, img_input_encode, local_faces_input, img_input):
    global ds_msv
    # ghi time vào ảnh
    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    cv2.putText(img_input, current_time, (0, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    try:
        # duyệt các khuôn mặt trong ảnh
        for i in range(0, len(img_input_encode)):
            faceloc = local_faces_input[i]
            cv2.rectangle(img_input,
                          (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (0, 0, 255), 2)
            #  duyệt các ảnh của sv. j là msv
            for j in imgList.keys():
                if len(imgList[j]) == 0:
                    continue
                #  img là data ảnh của mỗi sv
                for img in imgList[j]:
                    # so sánh khuôn mặt
                    faceDis = face_recognition.face_distance(img, img_input_encode[i])
                    matchIndex = np.argmin(faceDis)
                    if faceDis[matchIndex] < 0.40:
                        #  lấy vị trí của từng khuôn mặt và vẽ hình
                        cv2.putText(img_input, f"{j}", (faceloc[3], faceloc[2] + 27),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

                        if j not in ds_msv or len(ds_msv) == 0:
                            SaveDB(j, current_time)
                        else:
                            cv2.putText(img_input, "Registered", (faceloc[3], faceloc[2] + 54),
                                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        break
    except Exception as e:
        print(e)
    finally:
        return img_input


# mở cam, nhận dạng và gửi ảnh đến web
def gen_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        img_input_encoded = face_recognition.face_encodings(frame)
        local_faces_input = face_recognition.face_locations(frame)

        img_input = NhanDang(imgList, img_input_encoded, local_faces_input, frame)
        ret, buffer = cv2.imencode('.jpg', img_input)
        img_output = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img_output + b'\r\n')


# xem danh sách sinh viên
@app.route('/viewdssv')
def view_dssv():
    cap.release()  # giải phóng camera
    cv2.destroyAllWindows()  # thoát tất cả các cửa sổ
    global ds_sv
    ds_sv = dataSV.getDssv(Students.query.all())
    for student in ds_sv:
        print(student)
    return render_template('view_dssv.html', students=ds_sv)


# xóa 1 sinh viên trong danh sách
@app.route('/viewdssv/delete/<msv>', methods=['POST', 'GET'])
def DeleteSv(msv):
    global ds_msv
    global ds_sv
    global imgList
    if request.method == 'POST':
        if request.form.get('action') == 'Xác nhận':
            try:
                if msv in ds_msv:
                    ds_msv.remove(msv)
                print("ds_msv: ", ds_msv)
                # Xóa thư mục sử dụng shutil.rmtree()
                if os.path.exists(path + f'/{msv}'):
                    shutil.rmtree(path + f'/{msv}')
                Students.query.filter_by(msv=msv).delete()
                db.session.commit()
                # xóa ảnh sv
                imgList.pop(msv)
                for img in imgList:
                    print(img)
            except Exception as e:
                print(e)
            finally:
                return redirect(url_for('view_dssv'))
        return redirect(url_for('view_dssv'))
    student = Students.query.filter_by(msv=msv).first()
    return render_template('view_delete.html', student=student)


# cập nhật thông tin sinh viên
@app.route('/viewdssv/update/<msv>', methods=['POST', 'GET'])
def UpdateSv(msv):
    global ds_sv
    global imgList
    msv_old = msv
    error = None
    if request.method == 'POST':
        if request.form.get('action') == 'Xác nhận':
            msv_new = str(request.form['msv']).upper()
            name = str(request.form['fullname']).lower()
            name = name.title()
            if model_check.User_name(name) and model_check.User_msv(msv_new):
                student = Students.query.filter_by(msv=msv_old).first()
                try:
                    if msv_old != msv_new:
                        # thay đổi file ảnh và folder ảnh
                        path = 'D:/pythonProject_NhanDienKhuonMat/NhanDienKhuonMat_version2/static/imagesDB/' + msv_old
                        for file in os.listdir(path):
                            file = file.split('_')
                            os.rename(path + '/' + file[0] + '_' + file[1], path + '/' + msv_new + '_' + file[1])
                        os.rename(path, f'D:/pythonProject_NhanDienKhuonMat/NhanDienKhuonMat_version2/static/imagesDB/{msv_new}')
                        # cập nhập ảnh
                        imgList[msv_new] = imgList.get(msv_old)
                        imgList.pop(msv_old)
                        for img in imgList:
                            print(img)
                    # set info databasse
                    student.fullname = name
                    student.msv = msv_new
                    db.session.merge(student)
                    db.session.commit()

                except Exception as e:
                    print(e)
                finally:
                    return redirect(url_for('view_dssv'))
            else:
                error = 'Username/password không hợp lệ'
        return redirect(url_for('view_dssv'))
    student = Students.query.filter_by(msv=msv).first()
    return render_template('view_update.html', student=student, error=error)


# xem danh sách điểm danh
@app.route('/viewdsdd')
def view_dsdd():
    cap.release()  # giải phóng camera
    cv2.destroyAllWindows()  # thoát tất cả các cửa sổ
    return render_template('view_dsdd.html', dssv=dataSV.getDsdd(day))


# trang chủ--------------------------------
@app.route('/')
def index():
    global ds_sv
    ds_sv = Students.query.all()
    cap.release()  # giải phóng camera
    cv2.destroyAllWindows()  # thoát tất cả các cửa sổ
    return render_template('index.html')


# trang điểm danh-------------------------
# cập nhập danh sách điểm danh thời gian thực
@app.get('/update_dssv')
def update_dsdd():
    def generate():
        global ds_check_sv
        while True:
            dssv = ds_check_sv  # Lấy danh sách điểm danh từ cơ sở dữ liệu
            yield 'data: {}\n\n\n'.format(json.dumps(dssv))
            print("dsdiemdanh: ", dssv)
            ds_check_sv.clear()
            # time.sleep(0.5)

    return Response(generate(), content_type='text/event-stream')


# video nhận dạng của chức năng điểm danh
@app.route('/video_nhandang')
def video_nhandang():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


# trang chức năng điểm danh
@app.route('/checkSV')
def checkSV():
    return render_template("checkSV.html")


# tạo trang admin hoặc client, nếu name=admin
# trang thêm sv ----------------------------------------
@app.route('/video_themsv')
def video_themsv():
    return Response(SetPicture.SetImages(), mimetype='multipart/x-mixed-replace; boundary=frame')


# thêm ảnh sinh viên
@app.route('/addSV/images/<msv>')
def GetImages(msv):
    try:
        image_list = SetPicture.GetImages(msv)
        print(image_list)
    except Exception as e:
        print(e)
    finally:
        return render_template('imagesSV.html', image_list=image_list, msv=msv)


# xóa ảnh sinh viên
@app.route('/delete/image/<name>')
def DeleteImage(name):
    try:
        msv = name.split('_')[0]
        path_img = f'{msv}/{name}'
        SetPicture.DeteleImage(path_img)
    except Exception as e:
        print(e)
    finally:
        return redirect(url_for('GetImages', msv=msv))


# thêm sinh viên vào database và folder ảnh
@app.route('/addSV/<name>,<msv>', methods=['POST', 'GET'])
def SetImagesSV(name, msv):
    global ds_sv
    global imgList
    if request.method == 'POST':
        if request.form.get('action') == 'Lưu và Xem ảnh':
            try:
                SetPicture.DataSv(name, msv)  # tạo thư mục lưu ảnh
                msv_exist = Students.query.filter_by(msv=msv).first()  # kiểm tra xem sv đã tồn tại chưa
                if not msv_exist:  # nếu chưa thì thêm vào csdl
                    sv = Students(msv=msv, fullname=name)
                    db.session.add(sv)
                    db.session.commit()
                SetPicture.SaveImages(msv)  # lưu ảnh vào thư mục vừa tạo

                path_pic = f"D:/pythonProject_NhanDienKhuonMat/NhanDienKhuonMat_version2/static/imagesDB/{msv}"
                list_pic = os.listdir(path_pic)
                imgDB = []  # danh sách ảnh của 1 sinh viên
                for pic in list_pic:
                    img = cv2.imread(f"{path_pic}/{pic}")
                    encode = face_recognition.face_encodings(img)
                    imgDB.append(encode)
                imgList[msv] = imgDB
            except Exception as e:
                print(e)
            finally:
                return redirect(url_for('GetImages', msv=msv))
        elif request.form.get('action') == 'Hoàn tác':
            return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('setImagesSV.html', msv=msv)
    return render_template('setImagesSV.html', msv=msv)


# trang thêm sinh viên
@app.route('/addSV', methods=['POST', 'GET'])
def AddSV():
    cap.release()  # giải phóng camera
    cv2.destroyAllWindows()  # thoát tất cả các cửa sổ
    error = None
    if request.method == 'POST':
        if request.form['name'] and request.form['msv']:
            try:
                msv = str(request.form['msv']).upper()
                name = str(request.form['name']).lower()
                name = name.title()
                if model_check.User_name(name) and model_check.User_msv(msv):
                    msv_exist = Students.query.filter_by(msv=msv).first()
                    if msv_exist:
                        error = 'Sinh viên đã tồn tại'
                    else:
                        session['name'] = name
                        session['msv'] = msv
                        return redirect(url_for('SetImagesSV', name=name, msv=msv))
                else:
                    error = 'Họ tên hoặc mã sinh viên không hợp lệ'
            except Exception as e:
                print(e)
        else:
            error = 'Họ tên và mã sinh viên không được để trống'
    return render_template('addSV.html', error=error)


#  trang xử lý lỗi 404 ---------------------
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404


if __name__ == "__main__":
    try:
        if not os.path.exists("xla.db"):
            with app.app_context():
                db.create_all()

        app.run(host='0.0.0.0', port=5001, debug=True)
    except Exception as e:
        print(e)
    finally:
        cap.release()  # giải phóng camera
        cv2.destroyAllWindows()  # thoát tất cả các cửa sổ