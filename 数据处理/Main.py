import pandas as pd

# 读取Excel文件
file_path = 'data.xlsx'
df = pd.read_excel(file_path)
df['年月日'] = pd.to_datetime(df[['年', '月', '日']], format='%Y-%m-%d')

#print(df['年'])



