#1 đổi xau ra số nguyên
a = [int(x) for x in input().split()] 

#2 thêm giá trị vào list---------------------------
a=[]; a=a+[1,2]; a=a+[[1,2]]
#output: a=[1,2] ; a=[[1,2]]

#3 dao nguoc chuoi -----------------------------
s[::-1]; int(s[::-1])

#4 stack queue:---------------------------
a=[1,2,3,4]; a[len(a)-1]; a.pop(); a.append()
a=[1,2,3,4]; a[0]; a.remove(a[0]); a.append()

# kiem tra nguyen to-----------------------------
def nto(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) : # math.gcd
        if n % i == 0 : return False
    return True

# ma unicode----------------------------------
a='1'
print(ord(a))
print(chr(ord(a)+3)+'1')
print(int(chr(ord(a)+3))+1)
#49, 41, 5

# join-------------------------------------
a=[1,2,3]
s=set(a)
print(' '.join(str(x) for x in s))
# 1 2 3

# dem và thay thế--------------------------------
s='1212123124'
print(s.count('12')) # 4
print(s.replace('12','')) # 34
print(s.find('0')) # -1

# sort trong python------------------------------------
import functools
def cmp(x,y):
    if x<y: return 1
    return -1
a=[1,3,4,2,6]
a=sorted(a,key=functools.cmp_to_key(cmp))
a=sorted(sorted(sorted(a,key=lambda x:x.ma,reverse=True),key=lambda x:x.ten),key=lambda x:x.diem,reverse=True)
print(a)

m={'a':1,'c':4,'d':2}
s=sorted(m.items(), key=lambda item: item[1])
print(s)
s=sorted(m.items(), key=lambda item: -item[1])
print(s)

# dinh dang float------------------------------------
n=2.3356
"{:.2f}".format(n) # 2.33

# khoi tao mang 2 chieu---------------------------------------
a = [[]] * n
for i in range(n) :
    a[i] = [int(x) for x in input().split()]

# dinh dang ngay gio--------------------------------------------------
from datetime import datetime
date_string = "11/09/2020"
date_string1 = "26/09/2020"
date_object = datetime.strptime(date_string, "%d/%m/%Y")
date_object1 = datetime.strptime(date_string1, "%d/%m/%Y")
print("date_object =", date_object)
print("date_object1 =", date_object1)
print(date_object1-date_object)
n=str((date_object1-date_object))
print(n.split())

# datetime_object = datetime.datetime.now()
# print(datetime_object)

# date_object = datetime.date.today()
# print(date_object)

date_string = "11/09/2020 12:30:02"
date_string1 = "05/11/2020 09:20:05"
date_object = datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")
date_object1 = datetime.strptime(date_string1, "%d/%m/%Y %H:%M:%S")
print("date_object =", date_object)
print("date_object1 =", date_object1)
print(date_object1-date_object)

# doc file
file = open('a.txt','r',encoding='utf-8')
t= file.readline().strip('\n').strip()
for j in range(int(t)):
    h,c=[int(x) for x in file.readline().strip('\n').strip().split()]
    a=[[]]*h
    for l in range(h):
        a[l]=[int(x) for x in file.readline().strip('\n').strip().split()]
    print(a)