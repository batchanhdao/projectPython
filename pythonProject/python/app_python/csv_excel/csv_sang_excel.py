import pandas as pd

def csv_excel(pathCsv):
    df=pd.read_csv(pathCsv)
    df.to_excel(pathCsv,index=False)

pathCsv='DSHS.csv'
csv_excel(pathCsv)