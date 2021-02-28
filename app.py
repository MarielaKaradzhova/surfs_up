

# Local host
#localhost:5000


# Set Up the Flask Weather App
# Add dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Add sqlalchemy depencencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# Jsonify dependencies
from flask import Flask, jsonify

#Set Up Database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
#Reflect database into classes
Base = automap_base()
# Reflect database
Base.prepare(engine, reflect=True)
inspector=inspect(engine)
print(inspector.get_table_names())
# Save references to each table in database
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create session link from Python to Database
session = Session(engine)

# Set Up Flask
#Define Flask Application
app = Flask(__name__)

#Define the Welcome Route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
# Create the Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
    