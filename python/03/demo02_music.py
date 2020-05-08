from microbit import *
import music
import math

while True:
    amy = accelerometer.get_y()
    value = math.fabs(amy)
    music.pitch(value, 10)
