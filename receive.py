#!/usr/bin/env python

'''
This code is to be constantly run on the IOT device. It simply waits for a signal
to be sent from the defensive computer to signal that an attack has started. If signaled
the IOT device will do a system reboot as remediation.
'''
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

while 1:
	x = ser.readline()
	x = x.decode('utf-8')
	if x != '':
		os.system('reboot')
