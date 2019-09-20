import pandas as pd
import numpy as np
import os
from glob import glob
from datetime import datetime


os.getcwd()
os.chdir('D:\\RideItineraryPlanner\\theme park wait time data_csv\\WaltDisneyWorldMagicKingdom-Florida')
# allow ride input 
#ride=input('Enter a name:')
#print(ride)  
    
df=pd.read_csv('astro_orbiter.csv')

from fbprophet import Prophet
m = Prophet(changepoint_prior_scale=0.01).fit(df)
future = m.make_future_dataframe(periods=6000, freq='H')
future2 = future.copy()
future2 = future2[(future2['ds'].dt.hour > 7) & (future2['ds'].dt.hour < 22)]
fcst = m.predict(future2)
fig = m.plot(fcst)
fcst.to_csv('forecast\\astro_orbiter_fcst.csv',index=False)
m.plot_components(fcst)

