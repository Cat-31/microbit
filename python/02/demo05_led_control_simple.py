from microbit import *

interval = 1000
while True:
    pin1.write_digital(0)
    display.set_pixel(2, 2, 0)
    sleep(1000)

    pin1.write_digital(1)
    display.set_pixel(2, 2, 9)
    sleep(1000)
