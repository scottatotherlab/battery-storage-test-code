import datetime
import time
import os

clear = lambda: os.system('cls') # for clearing lines on the terminal

try:
    while True:
        dt = datetime.datetime.now()
        dtwom = dt.strftime("%Y-%m-%d %I:%M:%S") # datetime "dt" without milliseconds
        if (dt.second < 15):
            print("Time: " + str(dtwom) + "     Wall Power / Not Charging")
        elif (dt.second >= 15 and dt.second < 30):
            print("Time: " + str(dtwom) + "     Battery Power / Not Charging")
        elif (dt.second >= 30 and dt.second < 45):
            print("Time: " + str(dtwom) + "     Wall Power / Charging")
        else:
            print("Time: " + str(dtwom) + "     Battery Power / Charging")
        time.sleep(1)
        clear() # so only one line is shown on the console updated per sec
finally:
    clear() # clear terminal after ending scriptt