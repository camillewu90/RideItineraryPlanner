import pandas as pd
import numpy as np
import os
from glob import glob
from datetime import datetime
from datetime import datetime
import matplotlib.pyplot as plt


os.getcwd()
os.chdir('D:\\RideItineraryPlanner\\theme park wait time data_csv\\WaltDisneyWorldMagicKingdom-Florida\\ride')
# allow ride input 
#ride=input('Enter a name:')
#print(ride)  
    
df=pd.read_csv('astro_orbiter.csv')

fig=df.plot(x='ds',y='y')
fig.set_ylabel('wait time')
fig.set_xlabel('time')
plt.show()