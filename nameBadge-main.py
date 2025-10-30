# Imports go at the top
from microbit import *

while True:
    if button_a.is_pressed():
        display.scroll('I am Dusan')
    if button_b.is_pressed():
        display.scroll('hello nice to meat you!')