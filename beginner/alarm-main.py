from microbit import *
import music

music.set_tempo(bpm=180) 

def siren():
    while not button_b.was_pressed():
        for f in range(800, 1300, 8):   
            music.pitch(f, 10)
            if button_b.was_pressed(): return
                
    music.stop()
    
while True:
    if button_a.was_pressed():
        display.show(Image.SURPRISED)
        siren()
        display.clear()    

    if accelerometer.was_gesture('shake'):
        music.play(['C5:2','R:1'] * 3) 
    sleep(50)
        