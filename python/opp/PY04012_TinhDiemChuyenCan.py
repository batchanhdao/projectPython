class DSSV:
    def __init__(self,ma,ten,lop,diem) :
        self.ma=ma
        self.ten=ten
        self.lop=lop
        if diem<=0:
            self.diem=0
            self.ghichu='KDDK'
        else: 
            self.diem=diem
            self.ghichu=''
        
    def __str__(self):
        return self.ma+' '+self.ten+' '+self.lop+' '+ str(self.diem)+' '+self.ghichu
    def getMa(self):
        return str(self.ma)


n=int(input())
a=[]
ds=[]
for j in range(n):
    s=input()+'.'+input()+'.'+input()
    a.append(s)

for j in range(n):
    dd=input().split()
    diem=10
    for d in dd[1]:
        if d=='m':
            diem=diem-1
        elif d=='v':
            diem=diem-2
        else: diem=diem-0
    for d in a:
        ma=str(d).split('.')
        if dd[0]==ma[0]:
            ds.append(DSSV(ma[0],ma[1],ma[2],diem))

for d in a:
    ma = str(d).split('.')
    for j in ds:
        if ma[0]==j.getMa():
            print(j)
