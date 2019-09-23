import pandas as pd
import numpy as np
import os
from glob import glob
from datetime import datetime


os.getcwd()
os.chdir('D:\\RideItineraryPlanner\\theme park wait time data_csv\\WaltDisneyWorldMagicKingdom-Florida\\ride')
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
fcst.to_csv('D:\\RideItineraryPlanner\\theme park wait time data_csv\\WaltDisneyWorldMagicKingdom-Florida\\forecast\\astro_orbiter_fcst.csv',index=False)
m.plot_components(fcst)

from fbprophet.diagnostics import cross_validation
df_cv = cross_validation(m, initial='9000 hours', period='2000 hours', horizon = '20 hours')
df_cv.head()
from fbprophet.diagnostics import performance_metrics
df_p = performance_metrics(df_cv)
df_p.head()
from fbprophet.plot import plot_cross_validation_metric
fig = plot_cross_validation_metric(df_cv, metric='mae')


from pandas import Grouper
from matplotlib import pyplot
series = pd.read_csv('astro_orbiter.csv',index_col=0,parse_dates=True, squeeze=True)
series.ds=pd.to_datetime(series.ds)
series.day=
groups = series.groupby(Grouper(freq='A'))
years = pd.DataFrame()
for name, group in groups:
	years[name.year] = group.values
years.plot(subplots=True, legend=False)
pyplot.show()
print(series.head())
daily = series['ds'].groupby(pd.Grouper(freq='D'))

daily=series.groupby(series.index.hour).mean()
daily.plot()
pyplot.show()
