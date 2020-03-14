# 代码参考 https://mpython.readthedocs.io/zh/master/classic/breathing_light.html
import math
from microbit import *

def pulse(pin, period, gears):
    # 呼吸灯核心代码
    # 借用sin正弦函数，将PWM范围控制在 23 - 1023范围内
    # pin 输出引脚
    # period 呼吸一次的周期 单位/毫秒
    # gears 呼吸过程中经历的亮度档位数
    for i in range(2 * gears):
        pin.write_analog(int(math.sin(i / gears * math.pi) * 500) + 523)
        sleep(int(period / (2 * gears)))

while True:
    pulse(pin1, 2000, 100)