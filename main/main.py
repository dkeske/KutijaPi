__author__ = 'Keske'
import RPi.GPIO as GPIO
import time
from postServer import postServer,saveToFile
from threading import Thread 

def countCaps():
    GPIO.setmode(GPIO.BCM)

    ECHO = 23
    GPIO.setup(ECHO, GPIO.IN)
    broj = 0
    prethodni = 0
    while True:
        tekuci = GPIO.input(ECHO)
        
        if (tekuci == 0 and prethodni == 1):
            broj = broj + 1
            print(broj)
            if(broj==3):
            saveToFile(broj)
                broj = 0
               
        prethodni = tekuci
t1 = threading.Thread(target=countCaps, args=[])
t1.start()
