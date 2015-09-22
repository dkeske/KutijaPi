__author__ = 'Keske'
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ECHO = 23
GPIO.setup(ECHO, GPIO.IN)
broj = 0
while True:
	time.sleep(1)
    	print GPIO.input(ECHO)
        
