# Imports go at the top
from microbit import *

while True:
    display.show(Image.HAPPY)
    if button_a.is_pressed():
        display.show(Image.SAD)
    elif button_b.is_pressed():
        display.show(Image(
         "00000:" 
         "09090:"
         "00000:"
         "99999:"
         "00000:"
        ))
        
    sleep(200)
