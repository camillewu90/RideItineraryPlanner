import pandas as pd
import numpy as np
import os
from glob import glob
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

os.getcwd()
os.chdir('D:\\RideItineraryPlanner\\theme park wait time data_csv\\WaltDisneyWorldMagicKingdom-Florida')

df=pd.read_csv('test.csv')
df['time']=pd.to_datetime(df['time'])
df['date']=pd.to_datetime(df['date'])
df.info()
# interpolation
#df_copy=df.copy()
#df_copy.index=df_copy['time']
#del df_copy['time']
#df_copy.groupby(['weekofmonth','dayofweek']).resample('D').mean()



df_nm=df.iloc[21786:,:]
df_nm.head()
df_nm.isnull().sum()
df_nm=df_nm.fillna(method='ffill')
print(df_nm)
# plot time series by time
for column in df_nm.columns[1:-9]:
    fig=df_nm.plot(x='time',y=column)
    fig.set_ylabel('wait time')
    plt.show()
    
# smooth plot
    
wait_dsmooth=df_nm.rolling(window=1440).mean()
ax=wait_dsmooth.plot(y=wait_smooth[:,1])
ax.set_xlabel('time')
ax.set_ylabel('wait time')
ax.set_title('1440 window rolling mean of my time series')
plt.show()

print(df_nm.columns)
rides=list(df_nm.columns[1:])
print(rides)
#create new df for each ride
def select_ride(ride,df=df_nm):
    df_ride=df[['time',ride]]
    df_ride=df_ride.rename(columns={'time': "ds", ride: "y"})
    return(df_ride)
    
for column in df_nm.columns[1:-9]:
    df_temp=select_ride(column)
    df_temp.to_csv('{}.csv'.format(column),index=False)
    
# allow ride input 
#ride=input('Enter a name:')
#print(ride)  
    
tm=select_ride('tomorrowland_transit_authority_peoplemover')
fig=tm.plot(x='ds',y='y')
fig.set_ylabel('wait time')
plt.show()

print(tm)


