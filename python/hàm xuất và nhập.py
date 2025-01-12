# # hàm xuất
# from time import sleep
# s='abcd'
# def output():
#   print('hello',2,'\n',s)
#   print('hello',2,s,end='| |') # thay ký tự xuống dòng bằng ký tự bất kỳ
#   print('hello',2,s,sep='-') # thay khoảng trắng bằng ký tự bất kỳ
#   # ghi file
#   with open('a.txt','a',encoding='utf-8') as f:
#     print('bát chánh đạo', file=f)
#   for c in 'lê hồng ánh':
#     print(c,end='',flush=True)
#     sleep(0.1) # làm trễ
#   print()
# output()
# def in_put():
#   x=input('>>').split()
#   y=int(x[0])+5 ; print(y)
#   x[0]=int(x[0])
#   print(x) ; print(type(x))
# #in_put()

import json
import string


# Đọc dữ liệu từ file data.json
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# # Chuyển chuỗi JSON thành đối tượng Python
# data_dict = json.loads(json_data)

# Sinh tên sản phẩm
def generate_product_names(data):
    # Ghi kết quả vào file txt
    with open("product_names.txt", "w", encoding="utf-8") as file:
        # Tạo tất cả các mã từ AA1 đến ZZ10
        for letter1 in string.ascii_uppercase:
            for letter2 in string.ascii_uppercase:
                for i in range(1, 11):
                    code = f"{letter1}{letter2}{i}"
                    for item in data:
                        file.write(f"{item} {code}\n")
    return "Tên sản phẩm đã được ghi vào file 'product_names.txt'."


# # Lấy dữ liệu từ trường 'data' trong JSON
# product_data = data_dict['data']

# Sinh tên sản phẩm
# print(data)
for d in data:
    product_data = d['data']
    product_names = generate_product_names(product_data)
    print(product_names)
    # print(product_data)

