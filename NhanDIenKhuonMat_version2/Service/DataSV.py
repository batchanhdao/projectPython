import datetime
import functools
import os
import shutil
import time

from unidecode import unidecode


# sắp xếp sv theo alpha b -------------------------------------
def cmp(a, b):
    if unidecode(a.getLastname()) > unidecode(b.getLastname()):
        return 1
    elif unidecode(a.getLastname()) < unidecode(b.getLastname()):
        return -1
    else:
        if a.getLastname() > b.getLastname():
            return 1
        elif a.getLastname() < b.getLastname():
            return -1
        else:
            if unidecode(a.getFullname()) > unidecode(b.getFullname()):
                return 1
            elif unidecode(a.getFullname()) < unidecode(b.getFullname()):
                return -1
            else:
                if a.getFullname() > b.getFullname():
                    return 1
                elif a.getFullname() < b.getFullname():
                    return -1
                else:
                    return -1


# cmp end --------------------------------------------------------

class DataSV:
    def __init__(self):
        pass

    def getDsMSV(self, day):
        print("day" + str(day))
        dsMSV = []
        # thời gian
        # nếu file điểm danh chưa tồn tại
        if not os.path.exists(f"D:/pythonProject_NhanDienKhuonMat/NhanDienKhuonMat_version2/diemdanh{day}.txt"):
            # Tạo file
            with open(f"D:/pythonProject_NhanDienKhuonMat/NhanDienKhuonMat_version2/diemdanh{day}.txt", "w") as f:
                f.write('')
        else:
            try:
                file_open = open(f"D:/pythonProject_NhanDienKhuonMat/NhanDienKhuonMat_version2/diemdanh{day}.txt", "r", encoding="utf-8")
                lines = file_open.readlines()
                for line in lines:
                    # lấy msv
                    line = line.strip().split("-")
                    dsMSV.append(line[0])
            except Exception as e:
                print(e)
            finally:
                file_open.close()
        return dsMSV

    # lấy danh sách điểm danh đưa vào 1 list
    def getDsdd(self, day):
        dsdd = []
        print('-------------dsdd---------------')
        try:
            file_open = open(f"D:/pythonProject_NhanDienKhuonMat/NhanDienKhuonMat_version2/diemdanh{day}.txt", "r", encoding="utf-8")
            lines = file_open.readlines()
            for line in lines:
                # get dssv into 1 map
                ds = {}
                thongtin = line.strip().split("-")
                print(thongtin)
                ds['msv'] = thongtin[0]
                ds['name'] = thongtin[1]
                ds['time'] = thongtin[2]
                dsdd.append(ds)
        except Exception as e:
            print(e)
        finally:
            file_open.close()
        return dsdd

    # get dssv -------------------------------------------------------------
    def getDssv(self, students):
        students = sorted(students, key=functools.cmp_to_key(cmp))
        return students
