import RPi.GPIO as GPIO
import datetime
import time
import sys

# assign GPIO pin veriables
WallRelay = 5 
InverterRelay = 6
ChargerRelay = 13

# set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(WallRelay,GPIO.OUT)
GPIO.setup(InverterRelay,GPIO.OUT)
GPIO.setup(ChargerRelay,GPIO.OUT)

# assign descriptions for each state
state1 = "wall powering app / batt not charging"
state2 = "batt powering app / batt not charging"
state3 = "wall powering app / batt charging"
state4 = "batt powering app / batt charging"

# function that sets up each state - do not change the perametes here as you could damage the hardware!
def setRelays(state): 
    if state == state1: # turn off inverter power, wait 100 milliseconds, turn on wall power to app
        GPIO.output(InverterRelay, False)
        time.sleep(0.1)
        GPIO.output(WallRelay, True)
        GPIO.output(ChargerRelay, False)
    elif state == state2: # turn off wall power, wait 100 milliseconds, turn on inverter power to app
        GPIO.output(WallRelay, False)
        time.sleep(0.1)
        GPIO.output(InverterRelay, True)
        GPIO.output(ChargerRelay, False)
    elif state == state3: # turn off inverter power, wait 100 milliseconds, turn on wall power to app, then turn on the battery charger
        GPIO.output(InverterRelay, False)
        time.sleep(0.1)
        GPIO.output(WallRelay, True)
        GPIO.output(ChargerRelay, True)
    elif state == state4: # turn off wall power, wait 100 milliseconds, turn on inverter power to app, then turn on the battery charger
        GPIO.output(WallRelay, False)
        time.sleep(0.1)
        GPIO.output(InverterRelay, True)
        GPIO.output(ChargerRelay, True)
    else: # if a new/unrecognized state is introduced the program will end - this is to prevent damage to the hardware 
        GPIO.output(WallRelay, False)
        GPIO.output(InverterRelay, False)
        GPIO.output(ChargerRelay, False)
        print("unrecognized state --> stopping program!")
        sys.exit(0)

try:
    while True:
        dt = datetime.datetime.now()
        dtwom = dt.strftime("%Y-%m-%d %I:%M:%S") # format datetime "dt" in 12 hour time without milliseconds
        if (dt.second <= 15 or dt.second >= 45):
            setRelays(sta te1)
            print("Time: %s     %s"%(dtwom,state1))
        else:
            setRelays(state2)
            print("Time: %s     %s"%(dtwom,state2))
        time.sleep(1)

except KeyboardInterrupt:
    print (' --> User interupted the program!')

finally:
# cleanup the GPIO before finishing  :)
    GPIO.cleanup()
