# import tính
# so1=2; so2=2
# print(tính.cộng(so1,so2))
# print(tính.nhân(so1,so2))
try:
	file=open('a.txt','r',encoding='utf-8')
	# def đọc_từng_dòng():
	# 	data=file.readline()
	# 	print(data)
	# 	#return data
	# def readfile():
	# 	data=file.read()
	# 	print(data)
	# 	# đọc lại file 
	# 	file.seek(0) # vì con trỏ sẽ ở cuối văn bản sau khi đọc
	# 	data2=file.read() ; print(data2)
	# 	#return data
	# def chuyển_sang_list():
	# 	data=list(file)
	# 	print(data) ; print(data[0])
	# 	#return data
	# readfile()
	# #đọc_từng_dòng()
	# #chuyển_sang_list()
	# file.write('\n1234')
	# file.seek(0)
	# d=file.read(1000); print(d)
	# b=file.tell(); print(b) # vị trí của con trỏ
	l=[]; i=0
	while i<100:
		data_tmp=file.readline() 
		if len(data_tmp)==0: break
		if '1.'in data_tmp:
			data_tmp='giới định tuệ'
		elif '2.'in data_tmp:
			data_tmp='3 gốc - 3 độc'
		else: data_tmp='học hiểu hành'
		l.append(data_tmp)
		i=i+1
	print(l)
	file.close()
	file=open('a.txt','w',encoding='utf-8')
	file.write(str(l))

finally:
	file.close()
	# import os 
	# os.rename('aa.txt','a.txt')  đổi tên file
	# os.remove('a.txt')  xoá file

