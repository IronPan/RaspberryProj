import time
import RPi.GPIO as GPIO

# Uncomment to use BCM mode
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)

# Use BOARD mode
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

i = 1;
try:
    while True:
        # When use BCM, use 18
        # GPIO.output(18, i)
        GPIO.output(12, i)
        time.sleep(1)
        i = 1-i

except KeyboardInterrupt:
    print("Master interrupted me. I'll turn myself off.")
    
finally:
    GPIO.output(12, 0)
    print("I'll cleanup my GPIO.")
    GPIO.cleanup()
