import serial
from datetime import datetime
import re
import numpy as np
from threading import Thread
from rich import print
from imageBinParse import getByteList
import traceback
import os
import time
from PIL import Image

import updatesJSONHolder

#arduino = serial.Serial(port='/dev/cu.usbmodem14101', baudrate=500000, timeout=.1)

# Possible BUG first command probably doesnt work, so we may have to send HI first then do stuff after

currCommandI = 0
byteList = getByteList("kPhone.txt")

def read_packet():
    global currCommandI
    global byteList
    if currCommandI < len(byteList):
        command, data = byteList[currCommandI]
        currCommandI = currCommandI + 1
        return (command, data)
    else:
        print("Type [red bold]load[/ red bold] followed by the filepath to load new data ")
        print("Type [red bold]images[/ red bold] to put images in jpegImags folder")
        newCommand = input()
        if "load" in newCommand:
            newFile = newCommand[5:].strip() 
            byteList = getByteList(newFile)
            currCommandI = 0
            read_packet()
        elif "images" in newCommand:
            files = os.listdir("./images")
            for f in files:
                os.system(f'./ssdv -d ./images/{f} ./jpegImages/{f[:-4]}.jpeg')
            read_packet()
            #time.sleep(2)
            #for f in files:
            #os.system(f'./ssdv ./images/{} {}')
            #IMAGE STUFF
            #read_packet()

images = {}
image_start_times = {}

telemetry_data = None
try:
    telemetry_data = np.load('telemetry.npy')
except:
    pass

def packetParser(packet, miscInfo):
    try:
        dt, freqError, RSSI, SNR = miscInfo

        print(f'[bold blue]{packet[0]}')
        if packet[0][0] == 'P':
            image_id = int(packet[0][2:3])
            packet_number = int(packet[0][3:6])
            if packet[0][1] == 'S':
                camera_id = int(packet[0][6:])
                images[image_id] = [None]*packet_number
                image_start_times[image_id] = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
                printText = f'Receiving photo {image_id} from camera {camera_id} with {packet_number} packets; will be saved as {image_start_times[image_id]}.bin'
                print(printText)
                updatesJSONHolder.addToJSON(packet[0], "Image Data", printText, dt, freqError, RSSI, SNR, "")

            if packet[0][1] == 'D':
                printText = ""

                if image_id not in images:
                    images[image_id] = []
                    image_start_times[image_id] = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")

                    printText = printText + f'Missed start command for image {image_id} but receiving data; will be saved as {image_start_times[image_id]}.bin' + "\n"
                while len(images[image_id]) <= packet_number:
                    images[image_id].append(None)
                images[image_id][packet_number] = packet[1][:128]
                with open(f'images/{image_start_times[image_id]}.bin', 'wb+') as f:
                    for i in range(0, len(images[image_id]) - 1, 2):
                        if images[image_id][i] is not None and images[image_id][i + 1] is not None:
                            f.write(images[image_id][i])
                            f.write(images[image_id][i + 1])
                
                print(f'Received data packet {packet_number} for image {image_id}')
                printText = printText + f'Received data packet {packet_number} for image {image_id}'
                updatesJSONHolder.addToJSON(packet[0], "Image Data", printText, dt, freqError, RSSI, SNR, "")

            if packet[0][1] == 'E':
                camera_id = int(packet[0][6:])
                if image_id not in images:
                    images[image_id] = []
                    image_start_times[image_id] = datetime.now().strftime("%m-%d-%Y-%H:%M:%S")
                    print(f'Missed start command and all data for image {image_id}')
                else:
                    with open(f'images/{image_start_times[image_id]}.bin', 'wb+') as f:
                        for i in range(0, len(images[image_id]) - 1, 2):
                            if images[image_id][i] is not None and images[image_id][i + 1] is not None:
                                f.write(images[image_id][i])
                                f.write(images[image_id][i + 1])

                    # CONVERT IMAGE TO LINK

                    printText = f'Done receiving image {image_id} with {packet_number} packets; saving as {image_start_times[image_id]}.bin'

                    fileName = f'{image_start_times[image_id]}.bin'
                    os.system(f'./ssdv -d ./images/{fileName} ./jpegImages/{fileName[:-4]}.jpeg')
                    newImagePath = f'./jpegImages/{fileName[:-4]}.jpeg'
                    newImageLink = "http://127.0.0.1:8887" + "/" +  newImagePath
                    updatesJSONHolder.addToJSON(packet[0], "Image Finished", printText, dt, freqError, RSSI, SNR, newImageLink)

                    del images[image_id]

        elif packet[0][0] == 'T':
            telemetry = re.split('[|:]', packet[1].decode('utf-8'))
            data = ['0', telemetry[1], telemetry[2], telemetry[3], telemetry[5], telemetry[6], telemetry[7], telemetry[8], telemetry[9], telemetry[10]]
            data = [float(x) for x in data]
            data[0] = datetime.now().timestamp()
            if telemetry_data is None:
                telemetry_data = np.array([data])
            else:
                telemetry_data = np.concatenate([telemetry_data, np.array([data])], 0)
            np.save('telemetry.npy', telemetry_data)
            print(f'Received telemetry packet {packet[0][1:]}')

            printText = f'Received telemetry packet {packet[0][1:]}'
            updatesJSONHolder.addToJSON(packet[0], "Recevied Telemetry Packet", printText, dt, freqError, RSSI, SNR, "")

        elif packet[0][0] == 'R':
            with open('restarts.txt', 'a') as f:
                print('Arduino restart')
                f.write(datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + '\n')
            
            printText = "Arduino Restart"
            updatesJSONHolder.addToJSON(packet[0], "Arduino Restarting", printText, dt, freqError, RSSI, SNR, "")

        elif packet[0][0] == 'G':
            commandText = packet[1].decode("utf-8")
            commandText = commandText.strip()
            print(f'[dim]Ground Station Command [{commandText}]')

            printText = f'[dim]Ground Station Command [{commandText}]'
            updatesJSONHolder.addToJSON(packet[0], "Ran Ground Station Command", printText, dt, freqError, RSSI, SNR, "")

        elif packet[0][0] == "U":
            if packet[0][0:2] == "US":
                print("[bold green]Uplink Start!")
                updatesJSONHolder.addToJSON(packet[0], "Uplink Start", "", dt, freqError, RSSI, SNR, "")

            elif packet[0][0:2] == "UE":
                print("[bold green]Uplink End!")
                updatesJSONHolder.addToJSON(packet[0], "Uplink End", "", dt, freqError, RSSI, SNR, "")

            elif packet[0][0:2] == "UR":
                #TODO MIGHT HAVBE TO EDIT the [4:5] part
                print('[bold green]Restarting with Command: {packet[0][4:5]}')
                printText = 'Restarting with Command: {packet[0][4:5]}'
                updatesJSONHolder.addToJSON(packet[0], "Restarting Due to Command", printText, dt, freqError, RSSI, SNR, "")
        else:
            print(f'Couldn\'t parse packet {packet}')
            updatesJSONHolder.addToJSON(packet[0], "Could Not Parse Packet", "", dt, freqError, RSSI, SNR, "")
    except:
        traceback.print_exc()
        print('except')

#for b in byteList:
#    packetParser(b, ("", "", "", ""))

while (True):
    print("Type [red bold]load[/ red bold] followed by the filepath to load new data ")
    newCommand = input()
    if "load" in newCommand:
        newFile = newCommand[5:].strip() 
        byteList = getByteList(newFile)
        currCommandI = 0
        
        for b in byteList:
            packetParser(b, ("", "", "", ""))
    if "clear" in newCommand:
        os.system("rm -r ./images")
        os.system("rm -r ./jpegImages")
        os.system("mkdir ./images")
        os.system("mkdir ./jpegImages")
