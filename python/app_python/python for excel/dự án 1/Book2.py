import PySimpleGUI as sg 
import pandas as pd

read_file = pd.read_excel('D:\\pythonProject\\python\\python for excel\\dự án 1\\Book2.xlsx')
table_data = read_file.values.tolist()
table_heading = read_file.columns.values.tolist()

print(table_heading)
print(table_data)

# sg.theme("BlueMono")

# # noi dung
# layout = [
# 	[sg.Text("Enter Emloyee Information", size=(30,1), background_color="White", text_color="Orange", justification="Left")],
# 	[sg.Text('Emp ID', size=(10,1)), 
# 	sg.Input(key='ID', size=(61,4)), 
# 	sg.Text('     Department', size=(10,1)),
# 	sg.Combo(['Hành chính', 'Kỹ thuật kiểm tra giám sát','Kế hoạch tài chính','Truyền thống'],key='Department',size=(58,4))],

# 	[sg.Text('Emp Name', size=(10,1)), 
# 	sg.Input(key='Name', size=(61,4)), 
# 	sg.Text('     City', size=(10,1)),
# 	sg.Combo(['Hà Nội', 'Sài Gòn','Đà Nẵng'],key='City',size=(40,3))],

# 	[sg.Text('Gender', size=(10,1))],
# 	[sg.Radio("Male",'g',key='g1'),sg.Radio("Female",'g',key='g2')],

# 	[sg.Button('Save', key='Save'), sg.Button('Exit',key='Exit')],

# 	[sg.Table(values=table_data,
# 			headings=table_heading,
# 			key='Table',
# 			row_height=30,
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
# 		values['Gender']='Male' if values['g1'] else 'Female'
# 		del values['g1']; del values['g2']; del values['Table']

# 		read_file=read_file.append(values, ignore_index = True)
# 		read_file.to_excel('Book2.xlsx',index=False)

# 		read_file=pd.read_excel('Book2.xlsx')
# 		val = read_file.values.tolist()
# 		window['Table'].update(values = val)