from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import psycopg2
import pandas as pd
import os

os.getcwd()
os.chdir('D:\\RideItineraryPlanner')
# Define a database name (we're using a dataset on births, so we'll call it birth_db)
# Set your postgres username
dbname = 'parkride_db' #change this only according to your database name
username = 'postgres' #don't change this
password = 'Wyj329067!'#don't change this

## 'engine' is a connection to a database
## Here, we're using postgres, but sqlalchemy can connect to other things too.
engine = create_engine('postgresql://%s:%s@localhost:5432/%s'%(username,password,dbname))
print(engine.url)

## create a database (if it doesn't exist)
if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))

# read a database from CSV and load it into a pandas dataframe
mkridetimepred_data = pd.read_csv('predicted_wait_time.csv')
## insert data into database from Python (proof of concept - this won't be useful for big data, of course)
mkridetimepred_data.to_sql('mkridetimepred_data_table', engine, if_exists='replace')

# Connect to make queries using psycopg2
con = None
con = psycopg2.connect(database = dbname, user = username, password = password)

# when query date, need to type in format m/d/Y
sql_query = """
SELECT ds, astro_orbiter_yhat FROM mkridetimepred_data_table WHERE date='9/30/2019';
"""
mkridetimepred_data_from_sql = pd.read_sql_query(sql_query,con)
mkridetimepred_data_from_sql.head()
mkridetimepred_data_from_sql.shape
