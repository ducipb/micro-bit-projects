# Imports go at the top
from microbit import *
import random

while True:
    if accelerometer.was_gesture('shake'):
        number = random.randint(1, 6)
        if number == 1:
            display.show(Image(
            "00000:"
            "00000:"
            "00900:"
            "00000:"
            "00000"))
            sleep(1000)
            display.clear()
        elif number == 2:
            display.show(Image(
            "00000:"
            "00000:"
            "90009:"
            "00000:"
            "00000"))
            sleep(1000)
            display.clear()
        elif number == 3:
            display.show(Image(
            "00009:"
            "00000:"
            "00900:"
            "00000:"
            "90000"))
            sleep(1000)
            display.clear()
        elif number == 4:
            display.show(Image(
            "90009:"
            "00000:"
            "00000:"
            "00000:"
            "90009"))
            sleep(1000)
            display.clear()
        elif number == 5:
            display.show(Image(
            "90009:"
            "00000:"
            "00900:"
            "00000:"
            "90009"))
            sleep(1000)
            display.clear()
        else:
            display.show(Image(
            "90009:"
            "00000:"
            "90009:"
            "00000:"
            "90009"))
            sleep(1000)
            display.clear()