from microbit import *
steps=0

while True:
    if accelerometer.was_gesture('shake'):
        steps += 1
    if button_a.is_pressed():
        display.scroll(steps)
    if button_b.is_pressed():
        steps = 0