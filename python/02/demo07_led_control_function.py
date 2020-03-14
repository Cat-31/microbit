from microbit import *

def set_led(status, p_interval):
    pin1.write_digital(status)
    display.set_pixel(2, 2, status * 9)
    sleep(p_interval)

interval = 1000
while True:
    if button_a.is_pressed():
        interval -= 200
        if interval < 0:
            interval = 200
    elif button_b.is_pressed():
        interval += 200

    set_led(1, interval)
    set_led(0, interval)


