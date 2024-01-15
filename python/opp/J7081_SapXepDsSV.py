import functools

def cmp(x,y):
    if x.getTen()<y.getTen(): return 1
    elif x.getTen()>y.getTen(): return -1
    else:
        if x.getMa()>y.getMa(): return 1
        else: return -1

class DsSV:
    ma='';hoten='';sdt='';email=''
    ho='';dem='';ten=''
    def __init__(self,ma,hoten,sdt,email) :
        s=str(hoten).strip('\\n').split()
        self.ma=str(ma).strip('\\n').strip()
        self.hoten=str(hoten).strip('\\n').strip()
        self.sdt=str(sdt).strip('\\n').strip()
        self.email=str(email).strip('\\n').strip()
        self.ho=s[0]
        self.ten=s[len(s)-1]
        self.dem=s[1:len(s)-1]
    def __str__(self) :
        return self.ma+" "+self.hoten+" "+self.sdt+" "+self.email
    def getTen(self):
        return self.hoten
    def getMa(self):
        return self.ma
        
f = open("SINHVIEN.txt",'r')
li=[]
n=int(f.readline())
for i in range(n):
    ds=DsSV(f.readline(),f.readline(),f.readline(),f.readline())
    li.append(ds)
# li.sort(key=lambda x:(x.ten,x.ho,x.dem))
# li=sorted(li,key=functools.cmp_to_key(cmp))
li.sort(key=lambda x:(x.hoten),reverse=True)
for i in li:
    print(i)