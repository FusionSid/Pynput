from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

amount = input("How many time will it loop? ")
amount = int(amount)

time.sleep(5)

for i in range(amount):
    keyboard.press(Key.cmd)
    keyboard.press('v')
    keyboard.release(Key.cmd)
    keyboard.release('v')
    keyboard.release(Key.enter)

