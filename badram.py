import os
import serial
'''
This code is written to create near 100% CPU usage to represent a DOS attack on the IOT device.
Simply run with, "python3 badram.py" Only use this when testing for detection and baselining for malicious activities.
'''
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
ser.write('1'.encode())

os.fork()
os.fork()
os.fork()
os.fork()
os.fork()
os.fork()
os.fork()
while True:
	for i in range (11111000000000000000000000000000000000000000000000000000000000001111111111111111111111111111111111110,10000111111111111111111110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
		Gig=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009924*102999999999994*10999999999999999999999999999999999999999999999999999999924*5000
		a=9999900000000000000000000000000000000000000000000000000000000*(i*Gig)
		a=a*i*i*a*a*1000000000000000000000000000000000000000000000
		y=str(a*200000099999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009999999999999999999999999999999999999999999999999999999999999999999999999999999999990000000006)
		print (y)
		print(y)
		print(y)
		hostname="google.com"
		test=os.system('ping -c 10000000000000000000000' +hostname)
		with open('malicious.txt', "a") as f:f.write('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\n')
