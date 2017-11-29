#!/usr/bin/python3.5 python
#-*- coding: utf-8 -*-

"""Python Script for RaspberryPi3"""

#import modules
import RPi.GPIO as GPIO
import time
import sys

# setup pins

GPIO.setmode( GPIO.BOARD )
GPIO.setup( 3, GPIO.OUT )
GPIO.setup( 5, GPIO.IN )

#loop 5 times
try:
    for i in range(5):
        
        # flash  output pin 3 
        GPIO.output(3, GPIO.HIGH)
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
#except KayboardInterrupt:
    #pass
finally:
    GPIO.cleanup()

#sys.exit(0)
