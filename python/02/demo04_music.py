# 代码参考
# https://microbit-micropython.readthedocs.io/en/latest/tutorials/music.html

import music
from microbit import *

music.play(music.DADADADUM)
sleep(2000)

tune = ["C4:4", "D4:4", "E4:4", "C4:4", 
        "C4:4", "D4:4", "E4:4", "C4:4",
        "E4:4", "F4:4", "G4:8", "E4:4", 
        "F4:4", "G4:8"]
music.play(tune)