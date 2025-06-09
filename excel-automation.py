#Reads or writes Excel files using openpyxl or pandas.

import pandas as pd

df = pd.read_excel('data.xlsx')
df['Total'] = df['Price'] * df['Quantity']
df.to_excel('updated_data.xlsx', index=False)
