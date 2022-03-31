import json

def saveJSON(data, location):
    with open(location, "w") as write_file:
        json.dump(data, write_file)

def getJson(location):
    with open(location, "r") as read_file:
        data = json.load(read_file)
        return data

json = getJson("data.json")
# have this retrive from a file

def addToJSON(parsedData):
    command, commandMessage, datetime, freqError, RSSI, SNR, imageLink = parsedData
    dataVal = {
        "command": command,
        "commandMessage": commandMessage, 
        "datetime": datetime, 
        "freqError": freqError, 
        "RSSI": RSSI, 
        "SNR": SNR,
        "imageLink": imageLink
        }

    newJSON = {"data":[dataVal] + json["data"]}
    json = newJSON
    saveJSON(json, "data.json")
        

