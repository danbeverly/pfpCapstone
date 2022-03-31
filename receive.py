#!/usr/bin/env python

# Listening program waits to receive signal from the defensive laptop to trigger reboot 'remediation'

# import necessary libraries
import serial
import os

# set up serial communications
ser = serial.Serial(
	port = '/dev/ttyS0',
	baudrate = 115200,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
)

# read from serial and wait to receive signal to rebeoot
while 1:
	x = ser.readline()
	x = x.decode('utf-8')
	if x != '':
		# execute reboot
		os.system('reboot')
