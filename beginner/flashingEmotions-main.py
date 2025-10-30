# Imports go at the top
from microbit import *

display.clear()

while True:
    if button_a.is_pressed():
        for i in range(4):
         display.show(Image.HAPPY)
         sleep(200)
         display.clear()
         sleep(200)
    if button_b.is_pressed():
        for i in range(4):
            display.show(Image.SAD)
            sleep(200)
            display.clear()
            sleep(200)
    if accelerometer.was_gesture('shake'):
        for i in range(4):
            display.show(Image.SILLY)
            sleep(200)
            display.clear()
            sleep(200)
    if accelerometer.was_gesture('face down'):
        for i in range(8):
            display.show(Image.ANGRY)
            sleep(200)
            display.clear()
            sleep(200)
    
     
