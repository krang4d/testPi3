#!/usr/bin/python3.5 python
#-*- coding: utf-8 -*-

"""Python Script fo RaspberryPi3"""

#import modules
import RPi.GPIO as GPIO
import time

# setup [ims

GPIO.setmode( GPIO.BOARD )
GPIO.setup( 3, GPIO.OUT )
GPIO.setup( 5, GPIO.IN )

#loop 5 times
for i in range(5):
     # falsh  output pin 3 
     GPIO.output(3, GPIO.LOW)
     time.sleep(1)

     #read input pin 5
     if GPIO.input(5) == GPIO.HIGH:
          print( u"Pin 5 is on" )
     else:
          print( u"Pin 5 is off")

     GPIO.output(3, GPIO.LOW)
     time.sleep(1)

     #read input pin 5
     if GPIO.input(5) == GPIO.HIGH:
          print( u"Pin 5 is on" )
     else:
          print( u"Pin 5 is off")
