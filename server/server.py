from numpy import prod
from flask import Flask, request, jsonify

import updatesJSONHolder
import json

import os

import sys
sys.path.append("..")

from flask_cors import CORS
from flask_cors import cross_origin


app = Flask(__name__)
cors = CORS(app)

print("run with --prod for production server with correct address")

address = "http://localhost:8887/jpegImages/"
production = False
if ((len(sys.argv) > 2) and (sys.argv[1] == "--prod")):
      print("Attempting to run with production settings")
      address = "https://kazar4.com/SBUDNIC-Dashboard/server/jpegImages/" 
      production = True

@app.route('/getCommandData', methods=['GET'])
@cross_origin()
def getCommandData():

    data = updatesJSONHolder.getJSON("./data.json")["data"]
    for i in range(len(data)):
        if (data[i]["imageLink"] != ""):
          data[i]["imageLink"] = address + data[i]["imageLink"]
    data = {"data":data}
    
    return jsonify(data), 200

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

@app.route('/getGalleryLinkList', methods=['GET'])
@cross_origin()
def getImageLinkList():
    files = os.listdir("jpegImages")
    linksInfo = [{"link":(address + f), "fileName":f} for f in files]
    linksInfo = {"data":linksInfo}

    return jsonify(linksInfo), 200

if __name__ == '__main__':
    if (production):
      context = ('/ssl/server.crt', '/ssl/server.key') #certificate and key files
      app.run(host="0.0.0.0", port=1220, debug=True, ssl_context=context)
    else:
      app.run(host='0.0.0.0', port=1220)