class SV:
    ma=''
    ten=''
    diem=float(0)
    
    def __init__(self,ma,ten,d1) :
        if ma<10:
            self.ma='SV0'+str(ma)
        else: self.ma='SV'+str(ma)
        self.ten=ten
        self.diem=round(d1,2)
    def __str__(self) :
        return self.ma+" "+self.ten + str(self.diem)
    def getDiem(self):
        return self.diem
        
a=[]
liDiem=[]
for j in range(int(input())):
    liten=[x for x in input().split()]
    ten=''
    for l in liten:
        ten=ten+l[0].upper()+l[1:].lower()+' '
    d1=float(input())
    d2=float(input())
    d3=float(input())
    d=float((d1*3+d2*3+d3*2)/8)
    liDiem.append(round(d,2))
    a.append(SV(j+1,ten,d))
a.sort(key=lambda x:(x.diem),reverse=True)
for j in a:
    print(j,end=' ' )
    print(str(liDiem.index(j.getDiem())+1))