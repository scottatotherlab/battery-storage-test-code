# script for Wall power / charging battery during off peak hours and battery power during on peak hours
import RPi.GPIO as GPIO
import datetime
import time
import os

InverterRelay = 26 # switch between wall/battery power - wall should be "NC"
ChargerRelay = 20 # charger switch - should be "NO"

GPIO.setmode(GPIO.BCM)
GPIO.setup(InverterRelay,GPIO.OUT)
GPIO.setup(ChargerRelay,GPIO.OUT)
clear = lambda: os.system('clear') # for clearing lines on the terminal

# switch control: True = "NO"
try:
    while True:
        dt = datetime.datetime.now()
        dtwom = dt.strftime("%Y-%m-%d %I:%M:%S") # datetime "dt" without milliseconds
        # if (dt.hour <= 16 or dt.hour >= 21): # example for on/off peak hours
        if (dt.second <= 15 or dt.second >= 45): # quick example of logic
            print("Time: " + str(dtwom) + "     Wall power / charging battery") # on peak hours: 4pm - 9pm
            GPIO.output(ChargerRelay, True)
            GPIO.output(InverterRelay, False)
        else: 
            print("Time: " + str(dtwom) + "     Battery power") # off peak hours
            GPIO.output(ChargerRelay, False)
            GPIO.output(InverterRelay, True)
        time.sleep(1)
        clear() # so only one line is shown on the console updated per sec
finally:
# cleanup the GPIO before finishing :)
    GPIO.cleanup()
    clear() # clear terminal after ending script