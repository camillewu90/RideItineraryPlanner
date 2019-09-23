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
    df = pd.read_csv('D:\\RideItineraryPlanner\\predicted_wait_time.csv')
    df_sub=df[df['date'].str.match(visit_date)]
    df_subx=df_sub[['ds',ride_name]]
    print(df_subx)
    waittimes=[]
    for i in range(0,df_subx.shape[0]):
        waittimes.append(dict(time=df_subx.iloc[i]['ds'],wait_time=round(df_subx.iloc[i][ride_name])))
    return render_template("ride.html", waittimes = waittimes,visit_date = visit_date,ride_name = ride_name)
