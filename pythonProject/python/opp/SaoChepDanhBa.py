from datetime import datetime
file = open('SOTAY.txt','r')
data = file.readlines()
file.close()

class DanhBa:
    def __init__(self,ngay,ten,sdt):
        self.ten=ten
        t=str(ten).split()
        self.Ten=t[len(t)-1]
        self.HoDem=t[0:len(t)-1]
        self.sdt=sdt
        self.ngay=datetime.strptime(ngay,'%d/%m/%Y')
    def show(self) :
        return self.ten+': '+self.sdt+' '+self.ngay+'\n'
    def getTen(self):
        return self.Ten
    def getHoDem(self):
        return self.HoDem

ds=[]
ngay,ten,sdt='','',''
kt_ten=True
for l in data:
    l=l.strip('\\n').strip()
    if l[0:4]=='Ngay':
        ngay=l[5:]
    else:
        if kt_ten: 
            ten=l
            kt_ten=False
        else:
            sdt=l
            kt_ten=True
    if ngay!='' and ten!='' and sdt!='':
        ds.append(DanhBa(ngay,ten,sdt))
ds.sort(key=lambda x:(x.Ten,x.HoDem))
f=open('DIENTHOAI.txt','w')
for l in ds:
    f.write(l)
f.close()
