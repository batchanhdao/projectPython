def SET():
	set1={1,2,1,"anh",(3,4)}
	print(type(set1))
	print(set1)
	set2={1,(3,4),'le'}
	set3=set1|set2 ; print('hợp set1 và set2: '+ str(set3))
	set4=set1&set2 ; print('giao set1 và set2: '+ str(set4))
	set5=set3-set4 ; print(set5)
	set1-={2,'anh'} ; print('toán tử trừ: '+str(set1))
	#xoá phần tử đâu trong set
	print(set1.pop())
	#copy set
	set5=set1.copy() ; print(set5)
	#thêm phần tử vào set
	set1.add(10) ; print(set1)
	#truy xuất pt trong set
	for v in set1:
		print(v)
	# hàm max()/min() trả về giá trị lớn nhất/ nhỏ nhất trong set
	# hàm sorted(x,reverse=true/false) sắp xếp set theo giảm/tăng dần
	# hàm sum() trả về kết quả của các số trong set
# SET()
def DICT():
	# khởi tạo dict()
	d={'tên':'ánh','tuổi':20} ; print('khởi tạo dict(): ' + str(d))
	di={} ; print(di) ; print(type(di))
	# truy xuất pt trong dict
	print('value d[tên]: '+ str(d['tên']))
	# thêm pt vào dict
	di['tên']='a'; di['tuổi']=10
	print('thêm pt vào di: '+str(di))
	# truy xuất keys và values
	print('keys of di: '+ str(di.keys()))
	print('values of di: '+str(di.values()))
	li=list(di.keys())
	print(li)
	for i in di.values():
		print(i)
	# cập nhật dữ liệu
	di.update(d) ; print(di)
# DICT()

# di = {1:'a',2:'b'}
# # di1=di
# di1=di.copy()
# di1['1']='anh'
# # print(type(di))
# # print(di)
# # print(di1)
# # print(di1.get(1)) # lay value theo key
# # chuyen ve dang list
# liKey=list(di1.keys())
# print(liKey)
# for i in liKey:
# 	print(di1.get(i),end=" ")

# liValue=list(di1.values())
# print(liValue)

# for i,j in di1.items():
# 	print(i,j,end="|")

# di={1:0,2:0,3:0}
# # a=[1,3,1,1,2,3,3,3]
# # for i in a:
# # 	di[i]=di[i]+1
# print(di)

import math
def kt(i):
	if i<2: return 0
	for j in range(2,int(math.sqrt(i))+1):
		if i%j==0: return 0
	return 1
di={}
b=[0]*10
a=[1,2,3,4,5,6,7,8,9,10,11,2,3,4,3,5,2,3,7]
for i in set(a):
	di[i]=0
for i in a:
	if kt(i)==1:
		di[i]=di[i]+1
print(di)
print(b)
