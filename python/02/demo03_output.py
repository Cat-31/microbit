from microbit import *

# 需要一个蜂鸣器或是夹子线夹到耳机上
while True:
    pin0.write_digital(1)
    sleep(20)
    pin0.write_digital(0)
    sleep(480)