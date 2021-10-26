from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

start = input("Start: ")
end = input("End: ")
start = int(start)
end = int(end)


def count(start, end):
    while start != end:
        time.sleep(1)
        sta = f"{start}"
        keyboard.type(sta)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        start +=1

time.sleep(4)
count(start, end)