import RPi.GPIO as GPIO
import datetime
import time
import os

InverterRelay = 26 # switch between wall/battery power (wall should be normaly on)
ChargerRelay = 20 # switch charger on or off (should be normaly off)

GPIO.setmode(GPIO.BCM)
GPIO.setup(InverterRelay,GPIO.OUT)
GPIO.setup(ChargerRelay,GPIO.OUT)
clear = lambda: os.system('clear') # for clearing lines on the terminal

# switch control: True = "NO" terminal closes and "NC" terminal opens
try:
    while True:
        dt = datetime.datetime.now()
        dtwom = dt.strftime("%Y-%m-%d %H:%M:%S") # datetime "dt" without milliseconds
        if (dt.hour < 16 & dt.hour > 19):
            print("Time: " + str(dtwom) + "     Wall power / charging battery")
            GPIO.output(ChargerRelay, True)
            GPIO.output(InverterRelay, False)
        else: 
            print("Time: " + str(dtwom) + "     Battery power")  
            GPIO.output(ChargerRelay, False)
            GPIO.output(InverterRelay, True)
        time.sleep(1)
        clear() # so only one line is shown on the console updated per sec
finally:
# cleanup the GPIO before finishing :)
    GPIO.cleanup()
    clear() # clear terminal after ending script