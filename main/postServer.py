__author__ = 'Keske'
import requests

def postServer(number, isFull, boxID):
	payload = {'NumberOfCaps':number, 'isFull':isFull, 'Box':boxID}
	r = requests.post("http://192.168.0.101:8000/api/", data=payload)