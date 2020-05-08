from microbit import *
import random

while True:
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.show(str(random.randint(1, 6)))
