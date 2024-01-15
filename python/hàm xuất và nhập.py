# hàm xuất
from time import sleep
s='abcd'
def output():
  print('hello',2,'\n',s)
  print('hello',2,s,end='| |') # thay ký tự xuống dòng bằng ký tự bất kỳ
  print('hello',2,s,sep='-') # thay khoảng trắng bằng ký tự bất kỳ
  # ghi file
  with open('a.txt','a',encoding='utf-8') as f:
    print('bát chánh đạo', file=f)
  for c in 'lê hồng ánh':
    print(c,end='',flush=True)
    sleep(0.1) # làm trễ
  print()
output()
def in_put():
  x=input('>>').split()
  y=int(x[0])+5 ; print(y)
  x[0]=int(x[0])
  print(x) ; print(type(x))
#in_put()