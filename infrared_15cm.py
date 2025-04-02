import time
from Motor import *
import RPi.GPIO as GPIO
def distance():
    runningTotal = 0
    avgFactor = 30
    for x in range(avgFactor):
        v = (mcp.read_adc(2) / 1023.0) * 3.3
        distance1 = (16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 301.439)
        runningTotal = runningTotal + distance1
    else:
        distance = (runningTotal / avgFactor)

    return distance
