# Imports go at the top
from microbit import *

display.clear()

while True:
    display.show(Image(
        "00000:"
        "00900:"
        "09990:"
        "00900:"
        "00000"))
    sleep(500)
    display.show(Image(
        "00000:"
        "09990:"
        "09990:"
        "09990:"
        "00000"))
    sleep(500)
    display.show(Image(
        "90909:"
        "09990:"
        "99999:"
        "09990:"
        "90909"))
    sleep(500)
    display.show(Image(
        "90909:"
        "09090:"
        "90009:"
        "09090:"
        "90909:"
    ))
    sleep(500)
    display.show(Image(
        "90909:"
        "00000:"
        "90009:"
        "00000:"
        "90909:"
    ))
    sleep(500)
    display.clear()
    sleep(500)


    