import requests
import json
import signal
import serial
import os
import time

'''
This code is to be used as the main remediation method from the defensive computer.
It pipelines our response for timing how long the detection takes and how long reboot takes.
This code furthermore goes through stremed data on the API and parses it for what we want.
This also prints diagnostic of our remediation method.

Run this code when you are ready to remediate and read the EM sensor.
python3 workingRemediation.py
'''

def sendShutdown():
    ser.write(bytes("reboot", 'utf-8'))

#adapted code below to set up serial class. See citation [1],[3],[5]
ser = serial.Serial(
        port = '/dev/ttyUSB2',
        baudrate = 115200,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = 1
)

###code will mainly reside in API function loop.
#date, ID, IP, score, blank field containing a value for alert, instead of null (the last)

def api():
    #this is where the server for our data is hosted!
    api_site = 'http://localhost:8080/v1/get_runtime/1?sendIntervalSeconds=3'
    #for stream documentation and example to iterate through stream, we used citation [7]
    with requests.get(api_site, stream = True) as r:
        for event in r.iter_lines():
            #citation [9] for json.loads usage
            dicEvent = json.loads(event)
            if int(dicEvent['sigID']) == 1:
                print(dicEvent['sigID'])
                print("Flagged on pmon")
                return True
    ##continually needs to parse.
    #ingest stream


    ###if response is malicious break and immediately return True

def main():
    while True:
        x = ser.read().decode()
        print(x)
        response = False
        if x == '1':
            print("badram.py started")
            #get time of the start of the attack
            #used citation [8] to help us develop timing mechanism
            startTime = time.time_ns()
            response = api()
        if response == True:
            sendShutdown()
            #used citation [8] to help us develop timing mechanism
            endTime=time.time_ns()
            print("Sent shutdown")
            break
    # listen for signal from pi
    while True:
        try:
            x = ser.read().decode()
        except:
            x = 0
        if x == 'u' or x == 'p':
            #used citation [8] to help us develop timing mechanism
            rebootTime = time.time_ns()
            break
    #used citation [8] to help us develop timing mechanism
    totalTime = endTime - startTime
    rbTime = rebootTime - startTime
    totalTime = totalTime/(10**9)
    rbTime = rbTime/(10**9)
    print(str(totalTime) + " seconds total time.")
    print(str(rbTime) + " seconds of reboot total time.")
main()
