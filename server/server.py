from flask import Flask, request

import sys
sys.path.append("..")


app = Flask(__name__)

@app.route('/getCommandData', methods=['GET'])
def getCommandData():
    
    return "got text", 200

@app.route('/checkUplink', methods=['GET'])
def checkUplink():
    
    return "test is working"

@app.route("/lastTransmissionData", methods=['GET'])
def lastTransmissionData():
  
  return "OK", 200

@app.route("/telemetryData", methods=['GET'])
def telemetryData():
  
  return "OK", 200

@app.route('/getImageLinkList', methods=['GET'])
def getImageLinkList():

    return "test", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')