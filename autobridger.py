from pynput import keyboard
from pynput.mouse import Button, Controller as mController
from pynput.keyboard import Key, Listener, Controller as kController

import time

mouse = mController()
keyboard = kController()

def slow_bridge():
    time.sleep(5)
    keyboard.press(Key.shift)
    keyboard.press('s')
    keyboard.press('a')
    mouse.press(Button.right)
    time.sleep(100)


def speed_bridge():
    time.sleep(5)
    keyboard.press(Key.shift)
    keyboard.press('s')
    keyboard.press('a')
    mouse.press(Button.right)

    for i in range(100):
        time.sleep(0.5)
        keyboard.release(Key.shift)
        time.sleep(0.5)
        keyboard.press(Key.shift)


slow_bridge()