class SV:
    ma=''
    ten=''
    diem=float(0)
    kq=''
    def __init__(self,ma,ten,d1,dt,kv) :
        if ma<10:
            self.ma='TS0'+str(ma)
        else: self.ma='TS'+str(ma)
        self.ten=ten
        if dt!='Kinh':
            self.diem=self.diem+float(1.5)
        if kv==1: self.diem=self.diem+float(1.5)
        elif kv==2: self.diem+=float(1.0)
        self.diem+=d1
        if self.diem>=float(20.5): self.kq='Do'
        else: self.kq='Truot'
    def __str__(self) :
        return self.ma+" "+self.ten + '{:.1f}'.format(self.diem)+' '+self.kq
        
a=[]
for j in range(int(input())):
    liten=[x for x in input().split()]
    ten=''
    for l in liten:
        ten=ten+l[0].upper()+l[1:].lower()+' '
    d1=float(input())
    dt=input()
    kv=int(input())
    a.append(SV(j+1,ten,d1,dt,kv))
a.sort(key=lambda x:(x.diem),reverse=True)
for j in a:
    print(j)