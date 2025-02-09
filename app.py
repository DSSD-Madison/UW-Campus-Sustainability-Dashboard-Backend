from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    data = {"message": "specify a route like /api/[information]"}
    return jsonify(data), 200

# returns a list of all building names
@app.route('/api/building-names', methods = ['GET'])
def getBuildingNames():
    data = {"placeholder_message": "should return building names"}
    return jsonify(data), 200

# returns details for a specific building
@app.route('/api/building/<id>', methods = ['GET'])
def getBuildingDetails(id):
    data = {"placeholder_message": f'Building ID: {id}'}
    return jsonify(data), 200

# returns university information
@app.route('/api/university', methods = ['GET'])
def getUniversityInfo():
    data = {"placeholder_message": "Should return university information"}
    return jsonify(data), 200

# error handling
@app.errorhandler(404)
def page_not_found(error):
    data = {"message": "page not found"}
    return jsonify(data), 404

