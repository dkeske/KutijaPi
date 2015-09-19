__author__ = 'Keske'
import requests

def postServer(number, isFull, boxID):
	payload = {'NumberOfCaps':number, 'isFull':isFull, 'Box':boxID}
	r = requests.post("http://localhost:8000/api/", data=payload)