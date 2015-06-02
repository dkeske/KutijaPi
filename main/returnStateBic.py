__author__ = 'Keske'
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ECHO = 23
GPIO.setup(ECHO, GPIO.IN)
broj = 0
prethodni = 0
while True:
    tekuci = GPIO.input(ECHO)
    
    if tekuci == 0 and prethodni == 1:
        broj = broj + 1
        print broj
    prethodni = tekuci
