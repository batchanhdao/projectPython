import PySimpleGUI as sg

def ktSo(a,b):
    for i in range(0,len(a)):
        if a[i]>'9' or a[i]<'0': 
            if a[i]!='.':
                return False
    for i in range(0,len(b)):
        if b[i]>'9' or b[i]<'0': 
            if b[i]!='.':
                return False
    return True

def way1():
    sg.theme('DarkTeal7')  

    layout = [  [sg.Button('reset')],
                [sg.Text('Nhập số thứ nhất: '), sg.InputText(key='1')],
                [sg.Text('Nhập số thứ hai: '), sg.InputText(key='2')],
                [sg.Text('Chọn phép tính bạn cần: +, -, *, /: ')], 
                [sg.Button('+'), sg.Button('-'), sg.Button('*'), sg.Button('/')],    
                [sg.Text('Kết quả:',text_color='red',background_color='white'),
                sg.Text('', key='kq',text_color='red',background_color='white')],
                [sg.Text('Trạng thái:',text_color='red',background_color='white'),
                sg.Text(key='tt',text_color='red',background_color='white')],
                [sg.Button('exit')]

            ]

    # Create the Window
    window = sg.Window('Máy Tính', layout)
    while True:
        event, values = window.read() # event = giá trị nút Button values = giá trị input
        if event == sg.WIN_CLOSED or event == 'exit': # if user closes window or clicks cancel
            break
        else:
            trang_thai=''
            kq=0.0
            if event=='+': 
                if ktSo(values['1'],values['2']):
                    kq=float(values['1'])+float(values['2'])
                    trang_thai='Hợp lệ'
                else : trang_thai='Không hợp lệ'

            if event=='-': 
                if ktSo(values['1'],values['2']):
                    kq=float(values['1'])-float(values['2'])
                    trang_thai='Hợp lệ'
                else : trang_thai='Không hợp lệ'
                
            if event=='*': 
                if ktSo(values['1'],values['2']):
                    kq=float(values['1'])*float(values['2'])
                    trang_thai='Hợp lệ'
                else : trang_thai='Không hợp lệ'
                
            if event=='/': 
                if ktSo(values['1'],values['2']):
                    kq=float(values['1'])/float(values['2'])
                    trang_thai='Hợp lệ'
                else : trang_thai='Không hợp lệ'
                
            window['kq'].update(f"{kq:.3f}")
            window['tt'].update(trang_thai)
            if event=='reset':
                window['1'].update('')
                window['2'].update('')
    window.close()

way1()