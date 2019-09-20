import requests
from flask import render_template
from flask import request
from flaskexample import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2

user='postgres'
password = 'Wyj329067!'
host = 'localhost:5432'
dbname = 'parkride_db'
db = create_engine('postgresql://%s:%s@localhost:5432/%s'%(user,password,dbname))
con = None
con = psycopg2.connect(database = dbname, user = user,password = password)

#Standard home page. 'index.html' is the file in your templates that has the CSS and HTML for your app
@app.route('/input',methods=['GET', 'POST'])
def input():
    return render_template("input.html")

@app.route('/output',methods=['GET', 'POST'])
def output():
    #pull 'visit_date' from input field and store it
    visit_date = request.args.get('visit_date')
    ride_name = request.args.get('ride_name')
    #just select the Cesareans  from the birth dtabase for the month that the user inputs
    query = "SELECT ds, %s_yhat FROM mkridetimepred_data_table WHERE date='%s'"%(ride_name,visit_date)
    print(query)
    query_results=pd.read_sql_query(query,con)
    print(query_results)
    waittimes=[]
    for i in range(0,query_results.shape[0]):
        waittimes.append(dict(time=query_results.iloc[i]['ds'],wait_time=query_results.iloc[i]['%s_yhat'%ride_name]))
    return render_template("ride.html", waittimes = waittimes)
