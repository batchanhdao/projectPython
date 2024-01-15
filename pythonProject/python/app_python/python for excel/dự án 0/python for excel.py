def lấy_ghi_dữ_liệu():
	file = open('Book1.csv','r',encoding='utf-8')
	file_ghi = open('Book1_new.csv','w',encoding='utf-8')
	header=file.readline()
	list_header = header.strip();
	print(list_header[])
	file_ghi.write(header.strip()+';trung bình'+';Học lực\n');
	i=100
	while i>0:
		bien=file.readline(); 
		if bien == '': break
		bien_list=bien.split(';')
		toán=float(bien_list[2]); tin = float(bien_list[3])
		ave = (toán + tin)/2
		học_lực=''
		if ave>=8.0: học_lực='Giỏi'
		elif ave>=6.0: học_lực='Khá'
		elif ave>=4.0: học_lực='TB'
		else: học_lực='Kém'
		bien_ghi=bien.strip()+';'+str(ave)+';'+học_lực+'\n'
		print(bien_ghi)
		file_ghi.write(bien_ghi)
		bien_list.clear()
		i=i-1

def main():
	lấy_ghi_dữ_liệu()	
main()