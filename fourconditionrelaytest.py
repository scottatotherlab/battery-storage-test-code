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

try:
    while True:
        dt = datetime.datetime.now()
        dtwom = dt.strftime("%Y-%m-%d %I:%M:%S") # datetime "dt" without milliseconds
        if (dt.second < 15):
            GPIO.output(ChargerRelay, False) 
            GPIO.output(InverterRelay, False)
            print("Time: " + str(dtwom) + "     State 1/4 -- Wall Power / Not Charging")
        elif (dt.second < 30):
            GPIO.output(ChargerRelay, False) 
            GPIO.output(InverterRelay, True)
            print("Time: " + str(dtwom) + "     State 2/4 -- Battery Power / Not Charging")
        elif (dt.second < 45):
            GPIO.output(ChargerRelay, True) 
            GPIO.output(InverterRelay, False)
            print("Time: " + str(dtwom) + "     State 3/4 -- Wall Power / Charging")
        else:
            GPIO.output(ChargerRelay, True) 
            GPIO.output(InverterRelay, True)
            print("Time: " + str(dtwom) + "     State 4/4 -- Battery Power / Charging")
        time.sleep(1)
        clear() # so only one line is shown on the console updated per sec
finally:
# cleanup the GPIO before finishing :)
    GPIO.cleanup()
    clear() # clear terminal after ending scriptt