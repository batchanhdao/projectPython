def nhap():
	kt=True
	while(kt):
		so=input()
		kt=False
		for i in range(0,len(so)):
			if so[i]>'9' or so[i]<'0': 
				kt=True
				if so[i]=='.' and i!=0: kt=False
		if kt==False: 
			print('Số bạn điền:',so)
			return float(so)	
		else:
			print('Không nhận diện được số: ')	
			print('Nhập số')

while(True):
	print('Chọn phép tính bạn cần: +, -, *, /: ')
	s=input('Phép tính bạn chọn: ')
	if s=='exit': break
	if s!='+' and s!='-' and s!='*' and s!='/':
		print('Không nhận diện được phép tính: ')
	else:
		print('Nhập số thứ nhất: ')
		so1=nhap()
		print('Nhập số thứ hai: ')
		so2=nhap()
		kq=0.0
		if s=='+': kq=so1+so2
		if s=='-': kq=so1-so2
		if s=='*': kq=so1*so2
		if s=='/': kq=so1/so2
		print('Kết quả là:', kq)