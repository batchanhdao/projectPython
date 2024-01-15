# q=[1,2,3,4]
# print(type(q))  ;  print(q)
# print('h in hello world: '+str('h' in 'hello world'))
# a=16
# if a>18:
# 	print('trưởng thành')
# elif a>15:
# 	print('thanh niên')
# elif a>10:
# 	print('thiếu niên')
# else: print('trẻ con')
# # hàm for
# fruits=['a','b','c','d']
# fruits[:len(fruits)]=['chuối', 'na', 'táo', 'nho']
# # duyệt mảng
# # cách 1
# for fruit in fruits:
# 	fruit=fruit.upper()
# 	print('{:*^5}'. format('$') + fruit + '{:*^5}'. format('$'))
# # cách 2
# mang=[i*2 for i in range(5)]
# for j in range(len(mang)):
# 	print(mang[j])
# # xoá phần tử của mảng
# #del fruits[0]
# del fruits[1:3]
# print(fruits)
# #thêm phần tử vào mảng
# q.append(5)
# print(q)
# # hàm while
# while a<18:
# 	print(a)
# 	a=a+1
# # nối 2 mảng
# mang1=[1,2]; mang2=[3,4]; mang3=mang1+mang2+[5]
# print(mang3)
# # hàm gọi def
# def sosánh(a,b):
# 	return a>=b
# print(sosánh(1,2))

import vlc

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new("D:\\video\\video1.mp4")
Media.get_mrl()
player.set_media(Media)
player.play()

