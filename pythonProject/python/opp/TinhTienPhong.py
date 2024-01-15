# error str+int
# error date 0:00:00
# error '{:02d}'->'{:%02d}' java
# error '%d/%m/%Y' -> 'dd/mm/YYYY'
from datetime import datetime
class DsKH:
    def __init__(self,ma,ten,phong,days,phi) :
        self.ma='KH'+'{:02d}'.format(ma)
        self.ten=ten
        self.phong=phong
        self.days=days
        if phong[0]=='1':
            self.tong=phi+(days*25)
        elif phong[0]=='2':
            self.tong=phi+(days*34)
        elif phong[0]=='3':
            self.tong=phi+(days*50)
        else: self.tong=phi+(days*80)
    def __str__(self) :
        return self.ma+" "+self.ten+self.phong+' '+str(self.days)+' '+str(self.tong)
    def getTong(self):
        return self.tong 

def Ten(s):
    kq=''
    li=s.split()
    for j in li:
        kq=kq+j[0].upper()+j[1:].lower()+' '
    return kq
    
def Days(v,r):
    if v==r: return 1
    tong=str(r-v).split()
    return int(tong[0])+1

a=[]
file=open('KHACHHANG.in','r',encoding='utf-8')
t=int(file.readline().strip('\\n').strip())

for j in range(1,t+1):
    ten=Ten(file.readline().strip('\n').strip())
    phong=file.readline().strip('\n').strip()
    timeIn = datetime.strptime(file.readline().strip('\n').strip(),'%d/%m/%Y')
    timeOut = datetime.strptime(file.readline().strip('\n').strip(),'%d/%m/%Y')
    days=Days(timeIn,timeOut)
    phi = int(file.readline().strip('\n').strip())
    a.append(DsKH(j,ten,phong,days,phi))
a.sort(key=lambda x:(x.tong),reverse=True)
for j in a:
    print(j)