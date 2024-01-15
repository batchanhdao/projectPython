class GV:
    ma=''
    ten=''
    mon=''
    diem=float(0)
    kq=''
    def __init__(self,ma,ten,mon,d1,d2) :
        if ma<10:
            self.ma='GV0'+str(ma)
        else: self.ma='GV'+str(ma)
        self.ten=ten
        if mon[0]=='A': self.mon='TOAN'
        elif mon[0]=='B': self.mon='LY'
        else: self.mon='HOA'
        if mon[1]=='1':
            self.diem=d1+d2+float(2.0)
        elif mon[1]=='2':
            self.diem=d1+d2+float(1.5)
        elif mon[1]=='3':
            self.diem=d1+d2+float(1.0)
        else:self.diem=d1+d2
        if self.diem>=18: self.kq='TRUNG TUYEN'
        else: self.kq='LOAI'
    def __str__(self) :
        return self.ma+" "+self.ten+" "+self.mon+" " +'{:.1f}'.format(self.diem)+' '+self.kq
        
a=[]
for j in range(int(input())):
    ten=input()
    ma=input()
    d1=float(input())*2
    d2=float(input())
    a.append(GV(j+1,ten,ma,d1,d2))
a.sort(key=lambda x:(x.diem),reverse=True)
for j in a:
    print(j)