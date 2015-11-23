__author__ = 'Keske'
import requests

def postServer(number, isFull, boxID):
	payload = {'NumberOfCaps':number, 'isFull':isFull, 'Box':boxID}
	r = requests.post("http://192.168.0.101:8000/api/", data=payload)

def saveToFile(number):
	f = open('capLogs.txt', 'r+')
	old = f.read().strip()
	if not old.isdigit():
		old = 0
	new = int(old)+number
	f.seek(0)
	f.write(str(new))
	f.close()