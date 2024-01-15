import numpy as np
def kt(s):
    x=str(s)
    for j in range(0,len(x)-1):
        if int(x[j])>int(x[j+1]): return 0
    return 1

file1 = open('DATA!.in','rb')
file2 = open('DATA2.in','rb')
a1 = list(np.fromfile(file1, dtype=np.uint8))
a2 = list(np.fromfile(file2, dtype=np.uint8))
c=['a','b']
# a1=[]
# while(True):
#     l=len(a1)
#     n=int(file1.read(1))
#     a1.append(n)
#     if l==len(a1): break
# a2=[]
# while(True):
#     l=len(a2)
#     n=int(file2.read(1))
#     a2.append(n)
#     if l==len(a2): break
se=set(a1)
se=sorted(se)
for s in se:
    if kt(s)==1 and (s in a2):
        print(str(s)+' '+str(a1.count(s)+' '+str(a2.count(s))))
