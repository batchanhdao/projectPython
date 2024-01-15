import PySimpleGUI as sg # phát triển giao diện người dùng
import pandas as pd
# đọc file
read_file = pd.read_excel('Book1.xlsx') # đọc dữ liệu từ file chỉ định
# print(read_file)
# print('typedata: ', type(read_file)) # kiểu pandas

# lấy dữ liệu file đưa vào dạng list trong list
table_data = read_file.values.tolist()
# print(table_data[0][2]) # giấy
# print(table_data)
# print('typedata: ', type(table_data))

# lấy giá trị ở đầu mỗi cột vào trong list
table_heading = read_file.columns.values.tolist() 
# print(table_heading)
# print('typedata: ', type(table_heading))
head = read_file.head(2)
print(head)

# sg.theme("DarkBlue12")


# tạo form điền theo kiểu list
# layout = [
# 	[sg.Text("Nhập dữ liệu đơn hàng", size=(17,1), background_color="White", text_color="Orange", justification="Left")],
# 	[sg.Text('Mẫ', size=(10,1)), 
# 	sg.Combo(['A1','A2','B1','B2','C1','C2','D1','D2'],key='Mã',size=(40,4)),
# 	# sg.Input(key='ID', size=(61,4)), 
# 	sg.Text('     Tên hàng', size=(10,1)),
# 	sg.Combo(['giấy', 'vải bông','xi măng','gạch'],key='Tên hàng',size=(40,4))],

# 	[sg.Text('Ngày nhập', size=(10,1)), 
# 	sg.Input(key='Ngày nhập', size=(40,1)), 
# 	sg.Text('       Ngày bán' , size=(12,1)),
# 	sg.Input(key='Ngày bán',size=(40,1))],

# 	[sg.Text('số lượng', size=(10,1)), 
# 	sg.Input(key='số lượng ', size=(40,1)), 
# 	sg.Text('       đơn giá' , size=(12,1)),
# 	sg.Input(key='đơn giá ',size=(40,1))],

# 	# [sg.Text('Gender', size=(10,1))],
# 	# [sg.Radio("Male",'g',key='g1'),sg.Radio("Female",'g',key='g2')],

# 	[sg.Button('Save', key='Save'), sg.Button('Exit',key='Exit')],

# 	[sg.Table(values=table_data,
# 			headings=table_heading,
# 			key='Table',
# 			row_height=50,
# 			justification='center',
# 			expand_x=True,
# 			expand_y=True,
# 			)	
# 		]


# 	]

# window=sg.Window("Automated Data Entry From",layout)

# while True:
# 	event, values = window.read()
# 	if event ==sg.WIN_CLOSED or event == 'Exit':
# 		break
# 	if event=='Save':
# 		# values['Gender']='Male' if values['g1'] else 'Female'
# 		# del values['g1']; del values['g2']; 
# 		del values['Table']

# 		read_file=read_file.append(values, ignore_index = True)
# 		read_file.to_excel('Book1.xlsx',index=False)

# 		read_file=pd.read_excel('Book1.xlsx')
# 		val = read_file.values.tolist()
# 		window['Table'].update(values = val)