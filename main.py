from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

s = input("Start: ")
e = input("End: ")
s = int(s)
e = int(e)

def count(start, end):
    while start != end:
        time.sleep(1.5)
        sta = f"{start}"
        keyboard.type(sta)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        start +=1

count(s, e)