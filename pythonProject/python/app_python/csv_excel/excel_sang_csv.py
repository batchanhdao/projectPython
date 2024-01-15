import pandas as pd

def excel_csv(path):
    df=pd.read_excel('DSHS ĐẦU NĂM lớp 3A4- 22-23.xlsx')
    values=df.values.tolist()
    header=[values[4]]
    print(df[4:53])
    print(header)
    dshs=df[4:53]
    dshs.to_csv('DSHS.csv',index=False)

pathExcel=''
excel_csv(pathExcel)


