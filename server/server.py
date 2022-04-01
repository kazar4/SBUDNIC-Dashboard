from flask import Flask, request, jsonify

import updatesJSONHolder
import json

import sys
sys.path.append("..")

from flask_cors import CORS
from flask_cors import cross_origin


app = Flask(__name__)
cors = CORS(app)

@app.route('/getCommandData', methods=['GET'])
@cross_origin()
def getCommandData():
    
    return jsonify(updatesJSONHolder.getJSON("./data.json")), 200

@app.route('/checkUplink', methods=['GET'])
@cross_origin()
def checkUplink():
    
    return "test is working"

@app.route("/lastTransmissionData", methods=['GET'])
@cross_origin()
def lastTransmissionData():
  
  return "OK", 200

@app.route("/telemetryData", methods=['GET'])
@cross_origin()
def telemetryData():
  
  return "OK", 200

@app.route('/getImageLinkList', methods=['GET'])
@cross_origin()
def getImageLinkList():

    return "test", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1220)