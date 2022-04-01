#!/usr/bin/env python
'''
This code is intended to run automatically as part of the boot for measuring the timing of the reboot.
Place the execurtion of the code in the rc.local file, to automatically run on boot
Citation [11]
'''
while True:
    import serial
    import os
    
    #adapted code below to set up serial class. See citation [1],[3],[5]
    ser = serial.Serial(
    port = '/dev/ttyS0',
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
)
    #see citation [10] for the line of code below.
    ser.write('up'.encode())




