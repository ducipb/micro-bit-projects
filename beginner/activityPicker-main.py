from microbit import *
import random

while True:
    if button_a.is_pressed():
        random_number = random.randint(1, 8)
        if random_number == 1:
            display.scroll('learn python') 
        elif random_number == 2:
            display.scroll('learn a song on guitar')
        elif random_number == 3:
            display.scroll('go out')   
        elif random_number == 4:
            display.scroll('draw something')
        elif random_number == 5:
            display.scroll('read a book')
        elif random_number == 6:
            display.scroll('tidy your room')
        elif random_number == 7:
            display.scroll('watch a movie')
        else:
            display.scroll('play a board game')
            