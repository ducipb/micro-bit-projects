# Imports go at the top
from microbit import *
import random

while True:
    if accelerometer.was_gesture('shake'):
        number = random.randint(1, 4)
        if number == 3:
            display.show(Image.YES)
        elif number == 2:
            display.show(Image.NO)
        elif number == 4:
            display.scroll('maybe')
        else:
            display.show(Image.MEH)
    if button_a.is_pressed():
        display.clear()

        