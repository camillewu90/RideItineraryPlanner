import os
import pandas as pd
from datetime import datetime
os.getcwd()
os.chdir('D:\\RideItineraryPlanner')
df=pd.read_csv('theme park wait time data_csv\\WaltDisneyWorldMagicKingdom-Florida\\forecast\\predicted_wait_time.csv')
df.head()
df['ds']=pd.to_datetime(df['ds'])
df['date']=df['ds'].dt.date
df.to_csv('predicted_wait_time.csv',index=False)
df.head()