__author__ = 'Keske'
import Rpi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

ECHO = 23
GPIO.setup(ECHO, GPIO.IN)

while True:
    print(GPIO.input(ECHO))
