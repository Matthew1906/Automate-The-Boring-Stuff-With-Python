# GUI Automation

# y -> increase = down

import pyautogui

# size of screen
width, height = pyautogui.size()

# position of mouse
print(pyautogui.position())

# move to 10, 10 in 1.5 seconds
pyautogui.moveTo(10,10, duration = 1.5)

# move from current position, (offset)
pyautogui.moveRel(-400,50, duration=1)

pyautogui.click(10,10) #click in the coordinates

distance = 200
while distance>0:
    print(distance,0)
    pyautogui.dragRel(distance,0, duration=0.1)
    distance-=25
    print(0,distance)
    pyautogui.dragRel(0, distance, duration=0.1)
    print(-distance,0)
    pyautogui.dragRel(-distance,0, duration=0.1)
    distance-=25
    print(0,-distance)
    pyautogui.dragRel(0,-distance,duration=0.1)

# if the program gets out of control, just slam the cursor to the top-left
# -> more documentation in the internet



