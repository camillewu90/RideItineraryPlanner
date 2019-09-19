import pandas as pd
import numpy as np
import os
from glob import glob
from datetime import datetime
os.getcwd()
os.chdir('D:\\RideItineraryPlanner\\theme park wait time data_csv\\WaltDisneyWorldMagicKingdom-Florida')
os.getcwd()
filenames=glob('*.csv')
filenames.sort
print(filenames)
dataframes=[pd.read_csv(f) for f in filenames]
print(dataframes)
for df in dataframes:
    df['Time']=pd.to_datetime(df['Time'])
df_big=pd.concat(dataframes)
print(df_big.head())
df_big.to_csv("test.csv",index=False)
# then move the Time column to the first and remove the columns that are
# unique to the separate sheet, save it to big.csv