#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import serial


ser = serial.Serial(

    port='/dev/ttyS0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter=0
if  ser.is_open ==  True:
    ser.close()
while True:
    ser.open()
    #ser.write( b'Write counter: %d \n'%(counter) )
    str = 'write to ' + ser.name + ' counter: %d'%(counter)
    print ( str )
    #ser.write( str.encode('ascii') )
    ser.write(b'%s %d\n'%(str.encode('ascii'), counter) )
    print ( 'read from %s counter: %s\n'%(ser.name, ser.readline()) )
    ser.close()
    time.sleep(1)
    counter += 1
