from microbit import *

# 显示一个笑脸
display.show(Image.HAPPY)
sleep(1000)

# 自定义一个图案
boat = Image("05050:05050:05050:99999:09990")
display.show(boat)
sleep(1000)

# 一个小动画
left = Image("20000:20000:20000:20000:20000")
middle = Image("00600:00600:00600:00600:00600")
right = Image("00009:00009:00009:00009:00009")

images = [left, middle, right]
while True:
    display.show(images, delay=500)

