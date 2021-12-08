from pynput.mouse import Button, Controller as mController
from pynput.keyboard import Key, Listener, Controller as kController
import time

mouse = mController()
keyboard = kController()

def run():
    mouse.position = (388,974)
    mouse.click(Button.left, 3)
    time.sleep(0.1)
    keyboard.press(Key.cmd)
    keyboard.press('c')
    time.sleep(0.1)
    keyboard.release(Key.cmd)
    keyboard.release('c')
    time.sleep(0.1)
    mouse.position = (389,1033)
    mouse.click(Button.left)
    time.sleep(0.1)
    keyboard.press(Key.cmd)
    keyboard.press('v')
    time.sleep(0.1)
    keyboard.release(Key.cmd)
    keyboard.release('v')
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def on_press(key):
    pass

def on_release(key):
    if key == Key.esc:
        return False
    if key == Key.shift:
        run()

with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
