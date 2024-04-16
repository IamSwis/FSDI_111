from flask import Flask      #from the flask import module import the Flask class

app = Flask(__name__)   #create an instance of the Flask class

@app.get("/")   #Flask decorator tht maps view function to routes
def index():  #view function
    me= {           #python dictionary
        "first_name": "John",
        "last_name": "",
        "hobbies": "",
        "is_online": True
    }
    return me           #when you return a dictionary from a view function, it becomes JSON