s = 'abcdef'; print('chuỗi s: '+str(s))
s1 = """a
b
c"""
print('chuỗi s1: '+str(s1))

# ký tự xuống dòng
s2 = '\nabc' ; print(s2[0],s2[1],s2[2])

#chuỗi trần
print(r'abc\nabc')

# in chuỗi con
print(s[:]) # in toàn bộ chuỗi
print(s[:3]) # in chuỗi con vị trí 0 -> 2
print(s[2:]) # in chuỗi con vị trí cuối -> 2
print(s[1:4]) # in chuỗi con vị trí 1 -> 3

# hàm của chuỗi
# 1. độ dài chuỗi len(s) - s=abcdef
print('size(s) = ' + str(len(s)))
# 2. chuyển chuỗi hoa và thường
print('chuỗi hoa: '+str(s.upper()))  
print('chuỗi thường: '+str(s.lower()))  
# 3 thay thế chuỗi - replace()
print('thay thế chuỗi: '+str(s.replace('ab','anh')))
# 4. tách chuỗi - split()
ten = 'lê.hồng.ánh.tinh.tấn' ; print('tách chuỗi: ' + str(ten.split('.')))
# 5. nối chuỗi
a,b,c='le ','hong ','anh '
a=a+b+c ; a=a*3 ; print('toán tử cộng và nhân: '+str(a))
m = '{:*<5} {:*^5} {:*>5}'. format('a','a','a'); print(m)
if 'a'<=s[0]<='z' :
	print(s[0].upper())
	
	