import pyautogui
import math
import time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print('[*] Task initiated at', current_time)
print('[*] Loading script...')
print('[*] Running script...')
print('[*] Slicing cheese...')
print('[*] Feeding the rats...')
print('[*] Training the rats...')
time.sleep(3)
animation = "|/-\\"
idx = 0
while True:
    # Radius 
    R = 400
    # measuring screen size
    (x,y) = pyautogui.size()
    # locating center of the screen 
    (X,Y) = pyautogui.position(x/2,y/2)
    # offsetting by radius 
    pyautogui.moveTo(X+R,Y)
    #mouse move in circle
    for i in range(360):
        # setting pace with a modulus 
        if i%6==0:
            pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
            
    pyautogui.click(button='left')
    time.sleep(1)
    
    print('[',idx,'] In progress',animation[idx % len(animation)], end="\r")
    idx += 1
    

    



  
