from pynput.mouse import Controller, Button
import time

mouse = Controller()

time.sleep(4)
for i in range(5000):
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.05)