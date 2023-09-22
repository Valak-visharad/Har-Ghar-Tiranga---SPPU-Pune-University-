#code by vilakshan
#13.8.2022 ; 8 : 41 : 37 AM

#CONSTANTS
time_variable = 0.1
#pixel = (38,187)
#a = int(input("X : "))
#b = int(input("y : "))
pixel_bad = (17, 173)
pixel_save = (20, 223)
pixel_confused = (17,192)

#IMPORTS
from pynput.keyboard import Key, Listener, Controller
k = Controller()
#import os
import time
import pyautogui as cur

#pix1,pix2displayMousePosition()
cur.displayMousePosition()
#FUNCTIONS
def f5():
    k.press(Key.f5)
    k.release(Key.f5)

def on_press(key):
    pass

def on_release(key):
    if key == "B": # code to emulate 'crop'(mouse) and f5(keyboard) 15,173 BAD
        
        print("Bad Selected") ###TO BE COMMENTED
        cur.click(pixel_bad)
        cur.click(pixel_save) # CROP BUTTON
        time.sleep(time_variable)
        f5() # CHECKED_WORKING f5 key
        cur.moveTo(pixel_bad) # RETRIEVE CURSOR 
    
    elif key == "N": # code to emulate 'crop'(mouse) and f5(keyboard) 17,192  CONFUSED
        print("Confused Selected") ###TO BE COMMENTED
        cur.click(pixel_confused)
        cur.click(pixel_save) # CROP BUTTON
        time.sleep(time_variable)
        f5() # CHECKED_WORKING f5 key
        cur.moveTo(pixel_bad) # RETRIEVE CURSOR 
        
    elif key == "V": # code to emulate 'crop'(mouse) and f5(keyboard)  GOOD
        print("Good Selected") ###TO BE COMMENTED
        cur.click(pixel_save) # CROP BUTTON
        time.sleep(time_variable)
        f5() # CHECKED_WORKING f5 key
        cur.moveTo(pixel_bad) # RETRIEVE CURSOR


    
#MAIN
with Listener(on_press, on_release) as listener:
    listener.join()
 
