import functools
def cmp(x,y):
    if x.getDiem()<y.getDiem(): return 1
    elif x.getDiem()>y.getDiem(): return -1
    else:
        if x.getTen()<y.getTen(): return 1
        else: return -1
li=[]
class NV:
    ma=''
    ten=''
    diem=float(0)
    kq=''
    def __init__(self,ma,ten,diem):
        self.ma='TS0'+str(ma)
        self.ten=ten
        self.diem=diem
        if diem < 5: self.kq='TRUOT'
        elif diem <8: self.kq='CAN NHAC'
        elif diem <=9.5: self.kq = 'DAT'
        else: self.kq='XUAT SAC'
    def __str__(self):
        return self.ma+' '+self.ten+' '+'{:.2f}'.format(self.diem)+' '+self.kq
    def getDiem(self) :
        return self.diem
    def getTen(self):
        return self.ten
     
for i in range(int(input())):
    s=input()
    d1=float(input())
    d2=float(input())
    if float(d1)>10:
        d1=float(d1/10)
    if float(d2)>10:
        d2=float(d2/10)
    kq=(d1+d2)/2
    ds=NV(i+1,s,kq)
    li.append(ds)

# li.sort(key=lambda x: (x.diem ,x.ten),reverse=True)
li=sorted(li,key=functools.cmp_to_key(cmp))

for i in li:
    print(i)
