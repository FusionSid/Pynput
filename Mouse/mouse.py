from pynput.mouse import Controller, Button
import time

time.sleep(3)
mouse = Controller()
mouse.position = (957,152)
mouse.press(Button.left)
time.sleep(1)
mouse.release(Button.left)