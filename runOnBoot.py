#!/usr/bin/env python

# This file runs when the pi reboots, sending a signal to the defensive computer that the system is back up and running


while True:
    # import needed libraries
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
    # send 'up' to the devensive computer to signal that the pi has rebooted
    ser.write('up'.encode())




