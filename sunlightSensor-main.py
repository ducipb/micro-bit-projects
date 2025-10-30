# Imports go at the top
from microbit import *

while True:
    if display.read_light_level() > 17:
        display.show(Image(
        "90909:"
        "09990:"
        "99999:"
        "09990:"
        "90909"))
    else:
        display.show(Image(
             "00990:"
             "09900:"
             "09900:"
             "09900:"
             "00990:"         
        ))