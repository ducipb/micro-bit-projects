from microbit import *
import random

while True:
    if accelerometer.was_gesture('shake'):
        random_number = random.randint(1, 4)
        if random_number == 1:
            display.show(Image.ARROW_N)
        elif random_number == 2:
            display.show(Image.ARROW_E)
        elif random_number == 3:
            display.show(Image.ARROW_W)
        else:
            display.show(Image.ARROW_S)
    sleep(2000)
    display.clear()
            