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
# allow ride input 
#ride=input('Enter a name:')
#print(ride)  
    
df=pd.read_csv('dumbo_the_flying_elephant.csv')
df.head()

from fbprophet import Prophet
m = Prophet(changepoint_prior_scale=0.01).fit(df)
future = m.make_future_dataframe(periods=500000, freq='min')
future2 = future.copy()
future2 = future2[(future2['ds'].dt.hour > 7) & (future2['ds'].dt.hour < 23)]
fcst = m.predict(future2)
fig = m.plot(fcst)
fcst[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fcst.to_csv('dumbo_the_flying_elephant_fcst.csv',index=False)

m.plot_components(fcst)

