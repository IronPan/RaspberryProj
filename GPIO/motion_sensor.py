import time
import RPi.GPIO as GPIO
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)

status = 0
while True:
	tmpStatus = GPIO.input(14)
	if tmpStatus != status:
		status = tmpStatus
		print("Status Changed to " + ("DETECTED" if status == 1 else "UNDETECTED")
			 + " " + str(datetime.datetime.now()))
	time.sleep(0.1)

