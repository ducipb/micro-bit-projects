from microbit import *

count = 0
display.show(count)

while True:
    if accelerometer.was_gesture('shake'):
        count = 0
        display.scroll(count)
    elif button_b.is_pressed():
        count += 1
        display.scroll(count)
    elif button_a.is_pressed():
        display.scroll(count)
    sleep(100)
    