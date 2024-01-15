
# class HoaDon:
# 	def __init__(self,ma,ten,soCu,soMoi):
# 		self.ma="KH"+'{:02d}'.format(ma)
# 		self.ten=ten
# 		if soMoi-soCu<=50:
# 			tong=(soMoi-soCu)*100
# 			self.tong=round(tong+tong*2/100)
# 		elif soMoi-soCu<=100:
# 			tong=50*100+(soMoi-soCu-50)*150
# 			self.tong=round(tong+tong*3/100)
# 		else:
# 			tong=50*100+50*150+(soMoi-soCu-100)*200
# 			self.tong=round(tong + tong*5/100)
# 	def show(self):
# 		print(self.ma,self.ten,self.tong,sep=' ')

# ds=[]
# for j in range(int(input())):
# 	ds.append(HoaDon((j+1),input(),int(input()),int(input())))
# ds = sorted(ds,key=lambda x:x.tong,reverse=True)
# for j in ds:
# 	j.show()
# TÍCH LỚN NHẤT
a=[]
n=int(input())
a.extend([int(x) for x in input().split()])
a=sorted(a)
Max1=a[0]*a[1]
Max2=1
for j in range(len(a)-3,len(a)):
  Max2=Max2*a[j]
print(max(Max1,Max2))