from microbit import *

while True:
    if button_a.is_pressed():
        display.show('A')
    elif pin0.is_touched():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        break
    else:
        display.show(Image.SAD)

display.clear()
