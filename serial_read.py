#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import serial


ser = serial.Serial(

    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

if  ser.is_open == True:
    ser.close()

while 1:
    print( ser.name )
    ser.open()
    ser.write(b'%s\n'%(ser.name.encode('ascii')))
    x=ser.readline()
    print ( x )
    ser.close()
