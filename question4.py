import pandas as pd

df = pd.read_csv('BX-Books.csv',error_bad_lines=False,encoding='latin-1',sep=';')
df.head()