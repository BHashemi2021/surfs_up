
# Firs: In Anaconda Prompt or Windows CMD run:

# pip install Flask
# pip install psycopg2-binary

# Note: to see the results on the local webpage: save, run the code 
# (esp  if a dependency has been imported and reload the webpage)


from flask import Flask
from flask import jsonify

app = Flask(__name__)

hello_list = ["Hello", "world"]
hello_dict = {"Hello": "world"}


# set route 
# ('/' is the home directory)

@app.route('/')
def home():
    return "Hello world!!!!"

@app.route('/about')
def about():
    name = "Ben"
    location = "Toronto"
    
    return f'Hello, my name is {name}, I am in {location}'

@app.route('/contact')
def contact():

    return "This is my email ...."


# let's create a dictionary that the output will show as a json on the webpage
@app.route('/dict')
def dictionary():
    return hello_dict

@app.route('/jsonify')
def json():
    return jsonify(hello_list)



if __name__ == '__main__':
    app.run(debug=True)


# set FLASK_APP=app.py

# flask run