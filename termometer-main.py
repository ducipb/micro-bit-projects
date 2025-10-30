from microbit import *

while True:
    if button_a.was_pressed():
        display.scroll(temperature())
    if button_b.is_pressed():
        temp = temperature()
        if temp < 15:
            display.scroll('cold')
        elif temp < 25:
            display.scroll('comfortable')
        else:
            display.scroll('hot')

        