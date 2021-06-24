
# Firs: In Anaconda Prompt or Windows CMD run:

# pip install Flask
# pip install psycopg2-binary

# Note: to see the results on the local webpage: save, run the code 
# (esp  if a dependency has been imported and reload the webpage)


# from flask import Flask
# from flask import jsonify


# app = Flask(__name__)

# hello_list = ["Hello", "world"]
# hello_dict = {"Hello": "world"}


# # set the route 
# # ('/' is the home directory)

# @app.route('/')
# def home():

#     return "Hello world!!!!"


# @app.route('/about')
# def about():
#     name = "Ben"
#     location = "Toronto"
    
#     return f'Hello, my name is {name}, I am in {location}'


# @app.route('/contact')
# def contact():

#     return "This is my email ...."


# # let's create a dictionary that the output will show as a json on the webpage
# @app.route('/dict')
# def dictionary():
#     return hello_dict


# @app.route('/jsonify')
# def json():

#     return jsonify(hello_list)

## (This code is fro module would not run so other methods were use such as "return")
## flask run

# # To debug always add:
# if __name__ == '__main__':
#     app.run(debug=True)



# ---------------------------------------------------------------------------------------------------
# ####### The example codes above were all commented out, so that the rest of module be carried out. #########
# ---------------------------------------------------------------------------------------------------



# Setting Up the Flask Weather App

# import dependencies

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import app


# We'll set up our database engine for the Flask application 
engine = create_engine("sqlite:///hawaii.sqlite")


Base = automap_base()


# And to reflect (or copy) the database:
Base.prepare(engine, reflect=True)


# We'll create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station


# Finally, create a session link from Python to our database with:
session = Session(engine)


# We set Up a Flask by creating a Flask application called "app"
app = Flask(__name__)


# All of your routes should go after the app = Flask(__name__) line of code.


# We can define the welcome <<route>> using the code below:
@app.route("/")



# First, create a function welcome() with a return statement. 
# def welcome():
#    return



# Next, add the precipitation, stations, tobs, and temp routes that we'll need for this module into our return statement. 
# We'll use f-strings to display them for our investors:

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! <br>
    Available Routes:  <br>
    /api/v1.0/precipitation <br>  
    /api/v1.0/stations  <br>
    /api/v1.0/tobs  <br>
    /api/v1.0/temp/start/end
    ''')


# The next route we'll build is for the "precipitation analysis". 
@app.route("/api/v1.0/precipitation")


# Next, we will create the precipitation() function.
# def precipitation():
#    return

# Now we can add code to the function. 
# First, we  add the line of code that calculates the date one year ago from the most recent date in database.
# def precipitation():
#    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#    return

# Next, we write a query to get the date and precipitation for the previous year.
# def precipitation():
#    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#    precipitation = session.query(Measurement.date, Measurement.prcp).\
#       filter(Measurement.date >= prev_year).all()
#    return


# Finally, we'll create a dictionary with the date as the key and the precipitation as the value. 
# To do this, we will ""jsonify"" our dictionary. 
# Jsonify() is a function that converts the dictionary to a JSON file."

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   
   return jsonify(precip)



# (now it's time to move on to the third or the stations route. For this route we'll simply return a list of all the stations.)
@app.route("/api/v1.0/stations")


# (With our route defined, we'll create a new function called stations()	
# def stations():    
#     return

# (Now we need to create a query that will allow us to get all of the stations in our database.)
# def stations():
#     results = session.query(Station.station).all()
#     return

# (We want to start by unraveling our results into a one-dimensional array by the function np.ravel(), with results as our parameter.)
# So, we will convert our unraveled results into a list by a list function list(), and then convert that array 
# into a list. Then we'll jsonify the list and return it as JSON.
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# ! check the results on the local server by adding /api/v1.0/stations to the end of localhost URL http://127.0.0.1:5000/




# The goal is to return the temperature observations for the previous year. So we first create the route:
@app.route("/api/v1.0/tobs")


# Next, create a function called temp_monthly() 
# def temp_monthly():
#     return

# Now, we calculate the date one year ago from the last date in the database. 
# def temp_monthly():
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     return

# The next step is to query the primary station for all the temperature observations from the previous year.
# def temp_monthly():
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     results = session.query(Measurement.tobs).\
#         filter(Measurement.station == 'USC00519281').\
#         filter(Measurement.date >= prev_year).all()
#     return


# Finally, as before, unravel the results into a one-dimensional array and convert 
# that array into a list. Then jsonify the list and return our results
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


# (Our last route will be to report on the minimum, average, and maximum temperatures. 
# However, this route is different from the previous ones in that we will have to provide 
# both a starting and ending date.) 
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Next, create a function called stats() to put our code in.
# def stats():
#      return

# We need to add parameters to our stats()function: a start parameter and an end parameter. 
#  For now, set them both to None .
# def stats(start=None, end=None):
#      return


# With the function declared, we can now create a query to select the minimum, average, and maximum 
# temperatures from our SQLite database. We'll start by just creating a list called sel
# def stats(start=None, end=None):
#     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]


# Since we need to determine the starting and ending date, add an if-not statement to our code.
# We'll need to query our database using the list that we just made. Then, we'll unravel the results 
# into a one-dimensional array and convert them to a list. Finally, we will jsonify our results and return them.
# In the following code, take note of the asterisk in the query next to the sel list. 
# Here the asterisk is used to indicate there will be multiple results for our query: minimum, average, 
# and maximum temperatures.

# def stats(start=None, end=None):
#     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

#     if not end:
#         results = session.query(*sel).\
#             filter(Measurement.date >= start).all()
#         temps = list(np.ravel(results))
#         return jsonify(temps=temps)



# Now we need to calculate the temperature minimum, average, and maximum with the start and end dates. 
# We'll use the sel list, which is simply the data points we need to collect.

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

# Save and run the code and then open /api/v1.0/temp/start/end route and check to make sure you get 
# the correct result, which is: 
# [null,null,null]

# This code tells us that we have not specified a start and end date for our range. 
# Fix this by entering any date in the dataset as a start and end date.
# ! /api/v1.0/temp/2017-06-01/2017-06-30



# *To test your code, navigate to your project folder, surfs_up, for this module in the "command line". 
# * Then, run the following command will provide the localhost web address http://127.0.0.1:5000/
# * Then from the top left corner menu choose and add codes to the url find out about precipitations, stations, etc
#flask run


# ! Always add this code at the end of the code block to debug
if __name__ == '__main__':
    app.run(debug=True)





