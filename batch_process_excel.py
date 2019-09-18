import pandas as pd 
import glob
import os
os.getcwd()
os.chdir('D:\\RideItineraryPlanner')
#list all the xl file names with the folder
xls_file_names=os.listdir('theme park wait time data\\WaltDisneyWorldMagicKingdom-Florida')
# create a list of xls file path name 
xls=glob.glob('theme park wait time data\\WaltDisneyWorldMagicKingdom-Florida\\*.xlsx')

# create an empty csv file path list
csv=[]

if not os.path.exists('theme park wait time data_csv\\WaltDisneyWorldMagicKingdom-Florida'):
    os.mkdir('theme park wait time data_csv\\WaltDisneyWorldMagicKingdom-Florida')
# create a list of csv file path
for xls_file_name in xls_file_names:
    csv_temp='theme park wait time data_csv\\WaltDisneyWorldMagicKingdom-Florida\\'+xls_file_name.replace('xlsx','csv')
    csv.append(csv_temp)

# convert xls file to csv file
def xls_2_csv(xls_file,csv_file):
    read_file=pd.read_excel(xls_file)
    read_file.to_csv(csv_file,index=False)
 # finally convert the files   
for xls_f in xls:
    for csv_f in csv:
        xls_2_csv(xls_f,csv_f)

csv_list=glob.glob('theme park wait time data_csv\\WaltDisneyWorldMagicKingdom-Florida\\*.csv')
for csv in csv_list:
    df=pd.read_csv(csv)
    df1=df.apply(lambda x: pd.Series(x.dropna().values),1)
    df1.columns=df.columns[:-1]
    df1.columns.values[0]='Time'
    df1.to_csv(csv,index=False)

