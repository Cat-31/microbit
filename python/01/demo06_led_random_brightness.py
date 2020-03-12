# 导入模块
from microbit import *
import random

# 一直循环 不结束
while True:
    # 嵌套的循环
    for x in range(0, 5):
        for y in range(0, 5):
            # 随机亮度
            # 这是一个变量 名字叫 brightness
            brightness = random.randint(1, 9)
            display.set_pixel(x, y, brightness)
    sleep(1000)