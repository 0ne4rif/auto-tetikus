import pyautogui
import math
import time

time.sleep(5)

while True:
    # Radius 
    R = 400
    # measuring screen size
    (x,y) = pyautogui.size()
    # locating center of the screen 
    (X,Y) = pyautogui.position(x/2,y/2)
    # offsetting by radius 
    pyautogui.moveTo(X+R,Y)

    for i in range(360):
        # setting pace with a modulus 
        if i%6==0:
            pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
    
    time.sleep(1)

    pyautogui.click(button='left')

    



  

