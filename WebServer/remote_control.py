from flask import Flask
from multiprocessing import Pool
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

app = Flask(__name__)

def light_up():
    GPIO.output(12, 1)
    time.sleep(3)
    GPIO.output(12, 0)
    
        
@app.route('/')
def index():
    print('I got a request')
    pool = Pool(processes=1)
    pool.apply_async(light_up)
    return 'Hello worlds'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

GPIO.cleanup()  

