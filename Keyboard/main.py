# Keyboard
import typing_extensions
from pynput.keyboard import HotKey, Key, KeyCode, Listener, Controller
import sys
import time
from pynput.mouse import Controller, Button
import time

count = 0
keys = []

# Hotkeys/Keyboard Shortcuts
def hotkeys(): 
    def f1(): # End program
        sys.exit(0)


    def f2(): # Type text
        text = "Test"
        for i in range(100):
            keyboard = Controller()

            keyboard.type(text)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(0.5)


    def f3():
        mouse = Controller()
        time.sleep(4)
        for i in range(1000):
            mouse.press(Button.right)
            mouse.release(Button.right)
            time.sleep(0.0075)


    terminate = HotKey(
        [Key.cmd, Key.esc],
        f1
    )
    
    # KeyCode(char='')
    autoclick =  HotKey(
        [Key.cmd, KeyCode(char=']')],
        f3
    )


    type = HotKey(
        [Key.cmd, Key.shift],
        f2
    )

    hotkeys = [terminate, type, autoclick]


    def on_press(key):
        for hotkey in hotkeys:
            hotkey.press(l.canonical(key))


    def on_release(key):
        for hotkey in hotkeys:
            hotkey.release(l.canonical(key))


    with Listener(on_press=on_press, on_release=on_release) as l:
        l.join()



# Logs what i type and everytime i hit space it writes a new line
def keylogger():

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

hotkeys()

