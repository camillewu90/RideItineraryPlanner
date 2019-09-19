import os
import pandas as pd
from datetime import datetime
os.getcwd()

df=pd.read_csv('mk_ridetime_prediction.csv')
df.head()
df['ds']=pd.to_datetime(df['ds'])
df['date']=df['ds'].dt.date
df.to_csv('mk_ridetime_prediction.csv',index=False)
df.head()