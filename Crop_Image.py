#code by vilakshan
#13.8.2022 ; 8 : 41 : 37 AM

#CONSTANTS
time_variable = 0.3
pixel = (38,187)
a = int(input("X : "))
b = int(input("y : "))
pixel_back = (a, b)


#IMPORTS
from pynput.keyboard import Key, Listener, Controller
k = Controller()
#import os
import time
import pyautogui as cur


#FUNCTIONS
def f5():
    k.press(Key.f5)
    k.release(Key.f5)

def on_press(key):
    pass

def on_release(key):
    if key == Key.space: # code to emulate 'crop'(mouse) and f5(keyboard)
        print("Space pressed") ###TO BE COMMENTED
        cur.click(pixel) # CROP BUTTON
        time.sleep(time_variable)
        f5() # CHECKED_WORKING f5 key
        cur.click(pixel_back) # RETRIEVE CURSOR 
        

#MAIN
with Listener(on_press, on_release) as listener:
    listener.join()
