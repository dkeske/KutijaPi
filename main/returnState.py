__author__ = 'Keske'
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ECHO = 23
GPIO.setup(ECHO, GPIO.IN)
broj = 0
while True:
    if GPIO.input(ECHO)==1:
        broj = broj + 1
        print broj
        while GPIO.input(ECHO)==1:
            time.sleep(0.1)
            if GPIO.input(ECHO)==0:
                break
