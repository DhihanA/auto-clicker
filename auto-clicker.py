from time import sleep
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import threading

TOGGLE_KEY = KeyCode(char="q") # identifies the q key

mouse = Controller()
clicking = False # indicate if we are clicking or not, starts off not clicking

# does the actual clicking infinitely (until we toggle off ofc)
def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1) # 1 left-click
        sleep(0.001) # need this downtime otherwise it will always be clicking and we won't be able to toggle on/off

# toggles the clicking on/off
def toggle(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking # toggling

# putting the clicker in a separate thread, as the main thread is only used to check for the toggle
click_thread = threading.Thread(target=clicker)
click_thread.start()

# listener that calls the toggle func when any key is pressed
with Listener(on_press=toggle) as listener:
    listener.join()