# 导入模块
from microbit import display
from microbit import sleep


# 循环
for i in range(1, 3):
    display.show(i)
    sleep(1000)

# 遍历
for i in ('1', '5', '8'):
    display.show(i)
    sleep(1000)