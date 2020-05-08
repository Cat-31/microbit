from microbit import *

while True:
    reading = accelerometer.get_x()
    if reading > 30:
        display.show(">")
    elif reading < -30:
        display.show("<")
    else:
        display.show("-")