import pandas as pd
import os
import matplotlib.pyplot as mp # vẽ biểu đồ

path='C:\\Users\\Admin\\Downloads\\Thư mục mới\\'

filePaths=[]
megreFile = []
for file in os.listdir(path):
	if file.endswith('.csv'): # đuôi file
		filePath=pd.read_csv(path+file)
		filePaths.append(filePath)
		megreFile=pd.concat(filePaths) # gộp file excel



megreFile['Month']=megreFile['Order Date'].str[0:2] # tạo ô mới và lấy chuỗi
megreFile=megreFile[megreFile['Month']!='Or']
megreFile=megreFile.dropna(how='all') #bỏ giá trị nan
megreFile.to_csv('tohop2019.csv',index=False)
'*************tháng thu max***************'
print(megreFile['Month'].unique()) # xem các giá trị riêng
# ép kiểu
megreFile['Sale'] = pd.to_numeric(megreFile['Quantity Ordered'],downcast='float') * pd.to_numeric(megreFile['Price Each'],downcast='float')

# cắt cột và chèn
megreFile.insert(4,'Sale',megreFile.pop('Sale'))

# tính tổng doanh thu
sale_value = megreFile.groupby('Month').sum()['Sale']
print(sale_value)
print(sale_value.max())

# vẽ biểu đồ
months=range(1,13)
mp.bar(x=months, height=sale_value)
mp.xticks(months) # hiển thị tháng
mp.xlabel("tháng"); mp.ylabel('thu vào') # đặt tên hàng và cột
mp.show()

'*************city thu max***************'

print(megreFile['Purchase Address'].values[0])
city = lambda address:address.split(', ')[1] # hàm lấy giá trị city
megreFile['City']=megreFile['Purchase Address'].apply(city)
print(set(megreFile['City']))

# tính tổng doanh thu theo city
sale_value = megreFile.groupby('City').sum()['Sale']
print(len(sale_value)) # tính độ dài
print(sale_value)
print(sale_value.max())

# vẽ biểu đồ
#citys=megreFile['City'].unique()
citys=['Atlanta', 'Austin', 'Boston', 'Dallas', 'Los Angeles', 'New York City', 'Portland', 'San Francisco' , 'Seattle']
mp.bar(x=citys, height=sale_value)
mp.xticks(citys, rotation = 30, size = 8, color = 'Green') # hiển thị cities
mp.yticks(sale_value, color = 'Black')
mp.xlabel("thành phố"); mp.ylabel('thu vào') # đặt tên hàng và cột
mp.show()

'*************thời gian quảng cáo***************'

time = lambda address:address.split(' ')[1] # hàm lấy giá trị city
megreFile['Times']=megreFile['Order Date'].apply(time)
# print(sorted(set(megreFile['Times']), key=None, reverse=False))
# giờ bán nhiều nhất
megreFile['Hours']=megreFile['Times'].str[0:2]

# tính tổng doanh thu theo giờ
sale_value = megreFile.groupby('Hours').count()['Sale']
print(sale_value)
print(sale_value.max())

# vẽ biểu đồ
hours=sorted(set(megreFile['Hours']), key=None, reverse=False)
mp.plot(hours, sale_value)
mp.xticks(hours, rotation = 0, size = 10, color = 'Green') # hiển thị cities
mp.xlabel("thời gian"); mp.ylabel('thu vào') # đặt tên hàng và cột
mp.show()

'*************các sản phẩm thường đc bán cùng nhau***************'


groupProduct = lambda product: ', '.join(product)
df_dup=megreFile[megreFile['Order ID'].duplicated(keep=False)]
df_dup['All Products'] = df_dup.groupby('Order ID')['Product'].transform(groupProduct)
df_dup[['Order ID', 'All Products']].drop_duplicates()
print(df_dup['All Products'].value_counts().head(10))
print(df_dup)


megreFile=megreFile[megreFile['Month']!='Or']
megreFile=megreFile.dropna(how='all') #bỏ giá trị nan


'*************sản phẩm bán đc nhiều nhất***************'
# tính tổng từng loại sản phẩm đã bán
megreFile['Quantity Ordered'] = pd.to_numeric(megreFile['Quantity Ordered'],downcast='integer')
ordereds = megreFile.groupby('Product').sum()['Quantity Ordered']
print(ordereds)
print(ordereds.max())

# vẽ biểu đồ
products=['20in Monitor','27in 4K Gaming Monitor','27in FHD Monitor','34in Ultrawide Monitor','AA Batteries (4-pack)','AAA Batteries (4-pack)',
'Apple Airpods Headphones','Bose SoundSport Headphones','Flatscreen TV','Google Phone','LG Dryer','LG Washing Machine',
'Lightning Charging Cable','Macbook Pro Laptop','ThinkPad Laptop','USB-C Charging Cable','Vareebadd Phone',
'Wired Headphones','iPhone']
mp.bar(x=products, height=ordereds)
mp.xticks(products, rotation = 90, size = 8, color = 'Orange') # hiển thị cities
mp.xlabel("thời gian"); mp.ylabel('thu vào') # đặt tên hàng và cột
mp.show()

'*************giá từng sản phẩm***************'
megreFile['Prices']=pd.to_numeric(megreFile['Price Each'],downcast='integer')
prices = megreFile.groupby('Product').mean()['Prices']
print(prices)

'************* vẽ biểu đồ kép*****************'
x=products; y1 = ordereds; y2 = prices
fig, ax1 = mp.subplots()
ax2 = ax1.twinx()
ax1.bar(x,y1,color='g')
ax2.plot(x,y2,color='b')

ax1.set_xticklabels(products, rotation=90,size=8)
ax1.set_xlabel('Sản phẩm', color='Red')
ax1.set_ylabel('đơn bán', color='g')
ax2.set_ylabel('giá bán', color='b')
mp.show()

# lưu dữ liệu vào file
megreFile.to_csv('tohop2019.csv',index=False)
print(megreFile.head())
