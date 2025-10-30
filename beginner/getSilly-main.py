# Imports go at the top
from microbit import *

display.clear()

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    if button_b.is_pressed():
        display.show(Image.SAD)
    if accelerometer.was_gesture('shake'):
        display.show(Image.SILLY)
    if accelerometer.was_gesture('face down'):
        display.show(Image.ANGRY)