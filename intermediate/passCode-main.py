from microbit import *
import music

# === CONFIG ===
PASSCODE = "AABBA"
ENTRY_TIMEOUT_MS = 4000

# === SOUNDS ===
def success_sound():
    music.play(music.POWER_UP)

def failure_sound():
    music.play(music.WAWAWAWAA)

def tick():
    music.pitch(880, 80)

def tock():
    music.pitch(660, 80)

# === UI HELPERS ===
def prompt():
    display.show(Image.TARGET)
    sleep(600)
    display.scroll("CODE", wait=False, loop=False)

def clear_button_history():
    button_a.was_pressed()
    button_b.was_pressed()
    sleep(50)

# === INPUT ===
def read_sequence(length, timeout_ms):
    seq = []
    start = running_time()
    while len(seq) < length and running_time() - start < timeout_ms:
        # Single A press
        if button_a.was_pressed() and not button_b.is_pressed():
            seq.append('A')
            display.show('A')
            tick()
            sleep(150)
            display.clear()
        # Single B press
        if button_b.was_pressed() and not button_a.is_pressed():
            seq.append('B')
            display.show('B')
            tock()
            sleep(150)
            display.clear()
        # Cancel if A+B is pressed during entry (hold ~1s)
        if button_a.is_pressed() and button_b.is_pressed():
            # small hold to confirm cancel
            hold_start = running_time()
            while button_a.is_pressed() and button_b.is_pressed():
                if running_time() - hold_start > 800:
                    display.show(Image.NO)
                    failure_sound()
                    return None
                sleep(20)
        sleep(30)
    return seq if len(seq) == length else None  # None => timeout or cancel

# === MAIN LOOP ===
display.show(Image.ASLEEP)

while True:
    # Trigger: A+B together starts the passcode check
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.TARGET)
        sleep(200)
        prompt()
        clear_button_history()

        seq = read_sequence(len(PASSCODE), ENTRY_TIMEOUT_MS)

        if seq is None:
            # timeout or cancel
            display.show(Image.NO)
            failure_sound()
        else:
            if ''.join(seq) == PASSCODE:
                display.show(Image.YES)
                success_sound()
            else:
                display.show(Image.NO)
                failure_sound()

        sleep(600)
        display.clear()

        # small cooldown so we don't instantly retrigger
        while button_a.is_pressed() or button_b.is_pressed():
            sleep(30)

    sleep(50)
        