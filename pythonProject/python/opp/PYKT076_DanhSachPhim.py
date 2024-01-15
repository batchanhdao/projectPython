import functools 

class DSphim():
    def __init__(self,ma,tl,ngay,ten,tap):
        self.ma='P'+'{:03d}'.format(ma)
        self.tl=tl
        self.ngay=ngay
        self.ten=ten
        self.tap=tap
    def __str__(self):
        return self.ma+' '+self.tl+' '+self.ngay+' '+self.ten+' '+self.tap
    def getNgay(self):
        kq=str(self.ngay).split('/')
        return kq[2]+kq[1]+kq[0]
    def getTen(self):
        return self.ten
    def getTap(self):
        return self.tap

def cmp(a,b):
    if a.getNgay()>b.getNgay(): return 1
    elif a.getNgay()<b.getNgay(): return -1
    else:
        if a.getTen()>b.getTen(): return 1
        elif a.getTen()<b.getTen(): return -1
        else:
            if a.getTap()<b.getTap(): return 1
            else: return -1

ds=[]
tl={}
n,m=[int(x) for x in input().split()]
for j in range(1,n+1):
    tl['TL'+'{:03d}'.format(j)]=input().strip()
# print(tl.keys())
for j in range(1,m+1):
    ds.append(DSphim(j,tl[input()],input().strip(),input().strip(),input().strip()))
ds=sorted(ds,key=functools.cmp_to_key(cmp))
for h in ds:
    print(h)
