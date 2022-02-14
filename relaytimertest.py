import RPi.GPIO as GPIO
import datetime
import time
import os

InverterRelay = 26 # switch between wall/battery power (wall should be normaly on)
ChargerRelay = 20 # switch charger on or off (should be normaly off)

GPIO.setmode(GPIO.BCM)
GPIO.setup(InverterRelay,GPIO.OUT)
GPIO.setup(ChargerRelay,GPIO.OUT)
clear = lambda: os.system('clear') # clear terminal after ending script

# switch control: True = "NO" terminal closes and "NC" terminal opens
try:
    while True:
        dt = datetime.datetime.now()
        if (dt.second < 30):
            print("Time: " + str(dt.second) + ":     Wall power / charging battery")
            GPIO.output(ChargerRelay, True)
            GPIO.output(InverterRelay, False)
        else: 
            print("Time: " + str(dt.second) + ":     Battery power")  
            GPIO.output(ChargerRelay, False)
            GPIO.output(InverterRelay, True)
        time.sleep(1)
finally:
# cleanup the GPIO before finishing :)
    GPIO.cleanup()
    clear()