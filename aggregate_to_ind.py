import pandas as pd
import numpy as np
import os
from glob import glob
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go


os.getcwd()
os.chdir('D:\\RideItineraryPlanner')
#list all the xl file names with the folde
df=pd.read_csv('theme park wait time data_csv\\WaltDisneyWorldMagicKingdom-Florida\\test.csv')
rides=list(df.columns[1:-9])
print(rides)

def select_ride(ride,df):
    df_ride=df[['time',ride]]
    df_ride=df_ride.rename(columns={'time': "ds", ride: "y"})
    return(df_ride)
    
for ride in rides:
    df_temp=select_ride(ride,df)
    df_temp.to_csv('theme park wait time data_csv\\WaltDisneyWorldMagicKingdom-Florida\\ride\\{}.csv'.format(ride),index=False)

files=glob('theme park wait time data_csv\\WaltDisneyWorldMagicKingdom-Florida\\ride\\*.csv')
print(files)  
# drop duplicates
for file in files:
    df=pd.read_csv(file)
    df.drop_duplicates(inplace=True)
    df.to_csv(file,index=False)
