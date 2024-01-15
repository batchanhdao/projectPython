from tkinter import *
import pygame

pygame.mixer.init()
pygame.mixer.music.load("audio.mp3")

#---------------------------------------------------------------

def btClick(numbers):
	global operator
	pygame.mixer.music.play()
	operator=operator+str(numbers)
	textInput.set(operator)

def bt_AC():
	global operator
	pygame.mixer.music.play()
	operator=''
	textInput.set('')

def bt_DEL():
	global operator
	pygame.mixer.music.play()
	operator=operator[0:len(operator)-1]
	textInput.set(operator)

def bt_Bang(mode,i):
	global operator,listHis
	record=''
	result=0
	pygame.mixer.music.play()
# Standard
	if mode=='Standa':
		result=(eval(operator))
		operator=operator+' = '+ str(result)
		textInput.set(operator)
		record=operator
		operator=str(result)
#-----------------------------------------------------------
# Money
	if mode=='Money':
		kq=eval(operator)
		if Units==1: 
			result=str(kq)
			kq=(f'{(kq/23710):.2f}')
			operator=str(result)+'VND'+ "=" + str(kq) +'USD'
		if Units==2: 
			result=str(kq)
			kq=(f'{(kq/22974):.2f}')
			operator=str(result)+'VND'+ "=" + str(kq) +'Euro'
		if Units==3: 
			result=str(kq)
			kq=(f'{(kq/165):.2f}')
			operator=str(result)+'VND'+ "=" + str(kq) +'JPY'
		if Units==4: 
			result=str(kq)
			kq=(f'{(kq/3326):.2f}')
			operator=str(result)+'VND'+ "=" + str(kq) +'CNY'
		textInput.set(operator)
		record=operator
		operator=str(kq)
#-----------------------------------------------------------
# Weight
	if mode=='Weight':
		kq=eval(operator)
		if Units==1: 
			result=str(kq)
			kq=(f'{(kq/1000):.3f}')
			operator=str(result)+'kg'+ "=" + str(kq) +'tấn'
		if Units==2: 
			result=str(kq)
			kq=(f'{(kq*1000):.3f}')
			operator=str(result)+'kg'+ "=" + str(kq) +'gam'
		if Units==3: 
			result=str(kq)
			kq=(f'{(kq/0.45359237):.3f}')
			operator=str(result)+'kg'+ "=" + str(kq) +'pound'
		if Units==4: 
			result=str(kq)
			kq=(f'{(kq/0.0283495231):.3f}')
			operator=str(result)+'kg'+ "=" + str(kq) +'ounce'
		textInput.set(operator)
		record=operator
		operator=str(kq)
#-----------------------------------------------------------
# Measure
	if mode=='Measu':
		kq=eval(operator)
		if Units==1: 
			result=str(kq)
			kq=(f'{(kq/1000):.3f}')
			operator=str(result)+'m'+ "=" + str(kq) +'km'
		if Units==2: 
			result=str(kq)
			kq=(f'{(kq*1000):.3f}')
			operator=str(result)+'m'+ "=" + str(kq) +'mm'
		if Units==3: 
			result=str(kq)
			kq=(f'{(kq/0.0254):.3f}')
			operator=str(result)+'m'+ "=" + str(kq) +'inch'
		if Units==4: 
			result=str(kq)
			kq=(f'{(kq/0.3048):.3f}')
			operator=str(result)+'m'+ "=" + str(kq) +'foot'
		textInput.set(operator)
		record=operator
		operator=str(kq)
	# history
	for i in range(3,0,-1):
		listHis[i]=listHis[i-1]
	listHis[0]=record
	print(operator, result, listHis)

def bt_Mode2(s):
	global Statu,Unit,hangSo,Units
	pygame.mixer.music.play()
# Standard
	if s=='Standard':
		Statu=Status[0]
		Units=0
		Unit=""
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="",bg='white').grid(row=3,column=0)
		
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="",bg='white').grid(row=3,column=1)
		
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="",bg='white').grid(row=3,column=2)
		
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="",bg='white').grid(row=3,column=3)
# Money
#---------------------------------------------------------------------------------------------
	if s=='Money':
		textInput.set('Select:USD|Euro|JPY|CNY ')
		Statu=Status[1]
		Unit="VND"
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="USD",command=lambda:bt_Mode3('USD'),bg='white').grid(row=3,column=0)
		
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="Euro",command=lambda:bt_Mode3('Euro'),bg='white').grid(row=3,column=1)
		
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="JPY",command=lambda:bt_Mode3('JPY'),bg='white').grid(row=3,column=2)
		
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="CNY",command=lambda:bt_Mode3('CNY'),bg='white').grid(row=3,column=3)
# Weight
#---------------------------------------------------------------------------------------------		
	if s=='Weight':
		textInput.set('Select:tấn|gam|pound|ounce')
		Statu=Status[2]
		Unit="kg"
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="tấn",command=lambda:bt_Mode3('tấn'),bg='white').grid(row=3,column=0)
		
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="gam",command=lambda:bt_Mode3('gam'),bg='white').grid(row=3,column=1)
		
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="pound",command=lambda:bt_Mode3('pound'),bg='white').grid(row=3,column=2)
		
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="ounce",command=lambda:bt_Mode3('ounce'),bg='white').grid(row=3,column=3)
# Measure
#---------------------------------------------------------------------------------------------
	if s=='Measure':
		textInput.set('Select:km|mm|inch|foot ')
		Statu=Status[3]
		Unit="m"
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="km",command=lambda:bt_Mode3('km'),bg='white').grid(row=3,column=0)
		
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="mm",command=lambda:bt_Mode3('mm'),bg='white').grid(row=3,column=1)
		
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="inch",command=lambda:bt_Mode3('inch'),bg='white').grid(row=3,column=2)
		
		btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
		text="foot",command=lambda:bt_Mode3('foot'),bg='white').grid(row=3,column=3)

	btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
	text=Statu,bg='white').grid(row=1,column=1)

	btUnit=Button(cal, padx=30,bd=0,fg='black', font=('arial',15,'bold'),
	text=Unit,bg='white').grid(row=1,column=3)

def bt_Mode3(s):
	global Units
	pygame.mixer.music.play()
# Money
	if s=='USD': 
		Units=1
		textInput.set("VND --> USD | input values")
	if s=='Euro': 
		Units=2
		textInput.set("VND --> Euro | input values")
	if s=='JPY': 
		Units=3
		textInput.set("VND --> JPY | input values")
	if s=='CNY': 
		Units=4
		textInput.set("VND --> CNY | input values")
# Weight
#--------------------------------
	if s=='tấn': 
		Units=1
		textInput.set("kg --> tấn | input values")
	if s=='gam': 
		Units=2
		textInput.set("kg --> gam | input values")
	if s=='pound': 
		Units=3
		textInput.set("kg --> pound | input values")
	if s=='ounce': 
		Units=4
		textInput.set("kg --> ounce | input values")
# Measure
#--------------------------------
	if s=='km': 
		Units=1
		textInput.set("m --> km | input values")
	if s=='mm': 
		Units=2
		textInput.set("m --> mm | input values")
	if s=='inch': 
		Units=3
		textInput.set("m --> inch | input values")
	if s=='foot': 
		Units=4
		textInput.set("m --> foot | input values")

#---------------------------------------------------
def bt_listHis(i):
	pygame.mixer.music.play()
	for j in [0,1,2,3]:
		if i==j: textInput.set("History"+str(i+1)+": "+listHis[i])


cal=Tk()
cal.title('Calculator')
operator=''
textInput=StringVar()
hangSo=4
Status=["Standa","Money","Weight","Measu"]
Statu=Status[0]
Unit=""
Units=0
listHis=['','','',''] 

# Hiển thị - dòng đầu
txtDisplay=Entry(cal, width=25, font=('arial',20,'bold'),
	textvariable=textInput, bd=30, insertwidth=4, bg='aqua',
	justify='right').grid(columnspan=4)


# Dòng Modes1
#----------------------------------------------------------------
btMode=Button(cal, padx=18,bd=2,fg='black', font=('arial',15,'bold'),
	text='Mode:',bg='white',state=DISABLED).grid(row=1,column=0)

btStatus=Button(cal, padx=15,bd=0,fg='black', font=('arial',15,'bold'),
	text=Statu,bg='white').grid(row=1,column=1)

btDefault=Button(cal, padx=7,bd=2,fg='black', font=('arial',15,'bold'),
	text="Default:",bg='white',state=DISABLED).grid(row=1,column=2)


# Dòng Modes2
#----------------------------------------------------------------
btStandard=Button(cal, padx=5,bd=7,fg='black', font=('arial',15,'bold'),
	text='Standard',command=lambda:bt_Mode2('Standard'),bg='silver').grid(row=2,column=0)

btMoney=Button(cal, padx=12,bd=7,fg='black', font=('arial',15,'bold'),
	text="Money",command=lambda:bt_Mode2('Money'),bg='silver').grid(row=2,column=1)

btWeight=Button(cal, padx=10,bd=7,fg='black', font=('arial',15,'bold'),
	text="Weight",command=lambda:bt_Mode2('Weight'),bg='silver').grid(row=2,column=2)

btMeasure=Button(cal, padx=5,bd=7,fg='black', font=('arial',15,'bold'),
	text="Measure",command=lambda:bt_Mode2('Measure'),bg='silver').grid(row=2,column=3)

# numbers: DÒNG 1
#----------------------------------------------------------------
btOpen=Button(cal, padx=35,bd=8,fg='black', font=('arial',20,'bold'),
	text='(',command=lambda:btClick('('),bg='silver').grid(row=hangSo,column=0)

btDEL=Button(cal, padx=13,bd=8,fg='black', font=('arial',20,'bold'),
	text='DEL',command=lambda:bt_DEL(),bg='orange').grid(row=hangSo,column=1)

btAC=Button(cal, padx=20,bd=8,fg='black', font=('arial',20,'bold'),
	text='AC',command=lambda:bt_AC(),bg='orange').grid(row=hangSo,column=2)

btDir=Button(cal, padx=34,bd=8, fg='black', font=('arial',20,'bold'),
	text='/',command=lambda:btClick('/'),bg='silver').grid(row=hangSo,column=3)

# numbers: DÒNG 2
#----------------------------------------------------------------
hangSo+=1
bt7=Button(cal, padx=30,bd=8,fg='black', font=('arial',20,'bold'),
	text='7',command=lambda:btClick(7),bg='silver').grid(row=hangSo,column=0)

bt8=Button(cal, padx=30,bd=8,fg='black', font=('arial',20,'bold'),
	text='8',command=lambda:btClick(8),bg='silver').grid(row=hangSo,column=1)

bt9=Button(cal, padx=30,bd=8,fg='black', font=('arial',20,'bold'),
	text='9',command=lambda:btClick(9),bg='silver').grid(row=hangSo,column=2)

btMul=Button(cal, padx=30,bd=8,fg='black', font=('arial',20,'bold'),
	text='x',command=lambda:btClick('*'),bg='silver').grid(row=hangSo,column=3)

# numbers: DÒNG3
#----------------------------------------------------------------
hangSo+=2
bt4=Button(cal, padx=30,bd=8,fg='black', font=('arial',20,'bold'),
	text='4',command=lambda:btClick(4),bg='silver').grid(row=hangSo,column=0)

bt5=Button(cal, padx=30,bd=8,fg='black', font=('arial',20,'bold'),
	text='5',command=lambda:btClick(5),bg='silver').grid(row=hangSo,column=1)

bt6=Button(cal, padx=30,bd=8,fg='black', font=('arial',20,'bold'),
	text='6',command=lambda:btClick(6),bg='silver').grid(row=hangSo,column=2)

btSub=Button(cal, padx=34,bd=8,fg='black', font=('arial',20,'bold'),
	text='-',command=lambda:btClick('-'),bg='silver').grid(row=hangSo,column=3)

# numbers: DÒNG4
#----------------------------------------------------------------
hangSo+=3
bt1=Button(cal, padx=30,bd=8,fg='black', font=('arial',20,'bold'),
	text='1',command=lambda:btClick(1),bg='silver').grid(row=hangSo,column=0)

bt2=Button(cal, padx=30,bd=8,fg='black', font=('arial',20,'bold'),
	text='2',command=lambda:btClick(2),bg='silver').grid(row=hangSo,column=1)

bt3=Button(cal, padx=30,bd=8,fg='black', font=('arial',20,'bold'),
	text='3',command=lambda:btClick(3),bg='silver').grid(row=hangSo,column=2)

btAdd=Button(cal, padx=30,bd=8,fg='black', font=('arial',20,'bold'),
	text='+',command=lambda:btClick('+'),bg='silver').grid(row=hangSo,column=3)

# numbers: DÒNG5
#----------------------------------------------------------------
hangSo+=4
btClose=Button(cal, padx=34,bd=8,fg='black', font=('arial',20,'bold'),
	text=')',command=lambda:btClick(')'),bg='silver').grid(row=hangSo,column=0)

bt0=Button(cal, padx=30,bd=8,fg='black', font=('arial',20,'bold'),
	text='0',command=lambda:btClick(0),bg='silver').grid(row=hangSo,column=1)

btCham=Button(cal, padx=34,bd=8,fg='black', font=('arial',20,'bold'),
	text='.',command=lambda:btClick('.'),bg='silver').grid(row=hangSo,column=2)

btBang=Button(cal, padx=30,bd=8,fg='blue', font=('arial',20,'bold'),
	text='=',command=lambda:bt_Bang(Statu,Units),bg='silver').grid(row=hangSo,column=3)

# Calculation history 
#---------------------------------------------------------------- 
hangSo+=5
btHistory=Button(cal, padx=14,bd=4,fg='green', font=('arial',15,'bold'),
	text='Calculation history',bg='white').grid(row=hangSo,column=1,columnspan=2)

# Calculation
#----------------------------------------------------------------
hangSo+=6
btFirst=Button(cal, padx=20,bd=4,fg='black', font=('arial',15,'bold'),
	text='first',command=lambda:bt_listHis(0),bg='white').grid(row=hangSo,column=0)

btSecond=Button(cal, padx=10,bd=4,fg='black', font=('arial',15,'bold'),
	text='second',command=lambda:bt_listHis(1),bg='white').grid(row=hangSo,column=1)

btThird=Button(cal, padx=20,bd=4,fg='black', font=('arial',15,'bold'),
	text='third',command=lambda:bt_listHis(2),bg='white').grid(row=hangSo,column=2)

btFourth=Button(cal, padx=10,bd=4,fg='black', font=('arial',15,'bold'),
	text='fourth',command=lambda:bt_listHis(3),bg='white').grid(row=hangSo,column=3)

cal.mainloop()