# Imports go at the top
from microbit import *

for i in range(20):
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(250)
display.clear()    