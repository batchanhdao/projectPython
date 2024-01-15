import os
import win32com.client as win32
import smtplib
import ssl
from email.message import EmailMessage

working_directory = os.getcwd() 
# phương thức cho chúng ta biết vị trí của thư mục làm việc hiện tại
print(working_directory) 
# C:\Users\Admin\Drive của tôi (anhle12341710@gmail.com)\python\python for excel\dự án 2

name_folder = os.path.join(working_directory,'00a') # nối các đường dẫn lại với nhau
print(type(name_folder)) 
#C:\Users\Admin\Drive của tôi (anhle12341710@gmail.com)\python\python for excel\dự án 2\00a

wordApp = win32.Dispatch("Word.Application") # đọc tài liệu cho Microsoft Word
print(wordApp)

wordApp.Visible = True # Mở App

# Mở BẢNG ĐIỂM SV.docx = os
sourceDoc = wordApp.Documents.Open(os.path.join(working_directory, 'BẢNG ĐIỂM SV.docx'))

mail_merge = sourceDoc.MailMerge # Mở mailmerge
# Lấy data từ excel 
mail_merge.OpenDataSource(
	Name:=os.path.join(working_directory, 'Book1.xlsx'),
	sqlstatement:='SELECT * FROM [Data Source$]')

password='esimvqdfsyhqzpsl'

# gán data từ excel vào word
start=1; end=4
for i in range(start,end):
	mail_merge.DataSource.ActiveRecord = i 
	mail_merge.DataSource.FirstRecord = i 
	mail_merge.DataSource.LastRecord = i
	mail_merge.Destination = 0
	mail_merge.Execute(False)

	base_name = mail_merge.DataSource.DataFields('Họ_và_tên').Value # lấy trường data tên
	targetDoc = wordApp.ActiveDocument

	targetDoc.SaveAs2(os.path.join(name_folder, base_name + '.docx'),16) # tạo file word và đặt tên
	targetDoc.ExportAsFixedFormat(os.path.join(name_folder, base_name), exportformat:=17) # tạo file pdf và tên

	targetDoc.Close(False)
	targetDoc = None

	message = EmailMessage()
	message['Subject'] = f"Bang diem {base_name}"
	message['From'] = 'leanh17101601@gmail.com'
	message['To'] = mail_merge.DataSource.DataFields('email').Value
	message.set_content('Gui bang diem')
	attachmentPath = os.path.join(name_folder,base_name+'.pdf')
	with open(attachmentPath,'rb') as attachment:
		data = attachment.read()
		file_name = attachment.name
		message.add_attschment(data,maintype='application',subtype='pdf',filename=file_name)

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
		server.login('leanh17101601@gmail.com',password)
		server.sendmail('leanh17101601@gmail.com', mail_merge.DataSource.DataFields('email').Value,message.as_string())
	print('Success')	

sourceDoc.MailMerge.MainDocumentType = -1