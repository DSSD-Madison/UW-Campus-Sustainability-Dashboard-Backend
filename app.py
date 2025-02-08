from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# returns a list of all building names
@app.route('/api/building-names', methods = ['GET'])
def getBuildingNames():
    return "<p>should return building names</p>"

# returns details for a specific building
@app.route('/api/building/<id>', methods = ['GET'])
def getBuildingDetails(id):
    return f'<p>Building ID: {id} </p>' 

# returns university information
@app.route('/api/university', methods = ['GET'])
def getUniversityInfo():
    return "<p>Should return university information</p>"

