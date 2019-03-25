import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, queryMousePosition, PressKey, ReleaseKey, SPACE,moveMouseTo
import time
import math
import keyboard

actual_game_coords = [653, 585, 1142, 803]

game_coords = [666, 736, 1209, 962]
been_to = []

clicknum = 7

def dist(x0,y0,x1,y1):
    return math.sqrt(((math.fabs(x0-x1)) + math.fabs(y0-y1))**2)

def shoot():
    global clicknum
    been_to = []
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            if screen[y][x] < 10: #found black pixel - [0-255]
                Tooclose = False
                #check if been here
                for pos in been_to:
                    if dist(x,y,pos[0],pos[1]) < 50:
                        Tooclose = True
                        break
                if Tooclose:
                    continue
                #not been to
                #moveMouseTo(x+game_coords[0],y+game_coords[1]) #testing

                print(clicknum)
                if clicknum <= 1:
                    print('hit')
                    PressKey(SPACE)
                    clicknum = 7
                    time.sleep(0.5)


                click(x+game_coords[0] + 5,y+game_coords[1])
                click(x + game_coords[0]+ 5, y + game_coords[1]) #adding 3 and 5 since running too fast
                clicknum -= 2
                been_to.append([x,y])
                #time.sleep(0.01)

'''
#main loop
while True:
    mousepos = queryMousePosition()
    if mousepos.x <  1176:
        break

while True:
    # Quita
    mousepos = queryMousePosition()

    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        break

    screen = np.array(ImageGrab.grab(gamebox=game_coords))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY) #convert to grey image
    print(screen.shape())
    #shoot()
    #There is bullet to shoot
    #if screen[660,373] > 180:
        
'''


while True:
    if keyboard.is_pressed('a'):
        #Testing in paint
        screen = np.array(ImageGrab.grab(bbox=game_coords)) #shape is [y,x]
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY) #convert to grey image
        shoot()
        #moveMouseTo(586,397) #ammo box location
        #print(screen[586,397])

        #time.sleep(0.5)
