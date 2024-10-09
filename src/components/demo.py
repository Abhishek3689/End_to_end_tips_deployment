import os
import pandas as pd
print(os.getcwd())
df=pd.read_csv('data/tips.csv')
print(df.head())

