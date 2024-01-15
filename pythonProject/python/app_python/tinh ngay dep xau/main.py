import datetime

def ChuKy(total,chuky,sinh):
    li = list()
    for j in range(1,int(total/chuky)+1):
        tong=float(j)*chuky
        ngay=sinh+datetime.timedelta(days=tong)
        li.append(ngay.strftime('%H:%M:%S-%d/%m/%Y'))
    return li

def Giao2ChuKy(x,y,sinh):
    mx,my=[],[]
    for j in x:
        j=str(j).split('-')
        mx.append(j[1])
    for j in y:
        j=str(j).split('-')
        my.append(j[1])
    li=[]
    for j in mx:
        for l in my:
            if j==l:
                li.append(j)
                break
    return li
def Giao3ChuKy(x,y):
    mx=[]
    for j in x:
        j=str(j).split('-')
        mx.append(j[1])
    li=[]
    for j in mx:
        for l in y:
            if j==l:
                li.append(j)
                break
    return li

ngaySinh='2002/10/17'
theLuc=11.5 ; ngayTL=list()
tinhCam=14 ; ngayTC=list()
triTue=16.5 ; ngayTT=list()
giaoTL_TC=[]
giaoTC_TT=[]
giaoTT_TL=[]
giao3chuky=[]

ht = datetime.datetime.now()
sinh = datetime.datetime(*[int(i) for i in ngaySinh.split("/")])
soNgay=str(ht-sinh).split()

ngayTL.extend(ChuKy(int(soNgay[0])+1000,theLuc,sinh))
ngayTC.extend(ChuKy(int(soNgay[0])+1000,tinhCam,sinh))
ngayTT.extend(ChuKy(int(soNgay[0])+1000,triTue,sinh))
# print(ngayTL[0:10],ngayTC[0:10],ngayTT[0:10],sep='\n')


giaoTL_TC.extend(Giao2ChuKy(ngayTL,ngayTC,sinh))
giaoTC_TT.extend(Giao2ChuKy(ngayTC,ngayTT,sinh))
giaoTT_TL.extend(Giao2ChuKy(ngayTT,ngayTL,sinh))
print(giaoTL_TC,giaoTC_TT,giaoTT_TL,sep='\n-----\n')

giao3chuky.extend(Giao3ChuKy(ngayTT,giaoTL_TC))
print('giao3chuky')
print(giao3chuky)