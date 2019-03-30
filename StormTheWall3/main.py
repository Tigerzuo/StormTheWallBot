import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, PressKey, ReleaseKey, SPACE
import time
import keyboard

game_coords = [666, 736, 1209, 962]
ammo_coords = [656,386,686,396]
been_to = []

clicknum = 7

def dist(x0,y0,x1,y1):
    return math.sqrt(((math.fabs(x0-x1))**2 + (math.fabs(y0-y1))**2))

def shoot():
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            if screen[y][x] < 15: #found black pixel - [0-255]
                Tooclose = False
                #check if been here
                for pos in been_to:
                    if dist(x,y,pos[0],pos[1]) < 66:
                        Tooclose = True
                        break
                if Tooclose:
                    continue
                #not been to
                #moveMouseTo(x+game_coords[0],y+game_coords[1]) #testing

                print("hit", x,y,)

                click(x+game_coords[0] + 5,y+game_coords[1])
                click(x + game_coords[0]+ 5, y + game_coords[1]) #adding 3 and 5 since running too fast
                been_to.append([x,y])
                print(len(been_to))
                #time.sleep(0.01)
                if len(been_to) > 2:
                    del been_to[0]


def checkscreen():
    print(ammo_screen[2][2])
    print(ammo_screen[5][5])


while True:
    if keyboard.is_pressed('a'):
        while True:
            ammo_screen = np.array(ImageGrab.grab(bbox=ammo_coords)) #shape is [y,x]
            ammo_screen = cv2.cvtColor(ammo_screen, cv2.COLOR_BGR2GRAY)  # convert to grey image

            #checkscreen()
            #shoot()

            if ammo_screen[5][5] > 200: #ammo empty
                PressKey(SPACE)
                time.sleep(0.05)
                ReleaseKey(SPACE)
                time.sleep(0.5)

            if ammo_screen[5][5] < 190: #ammo full
                screen = np.array(ImageGrab.grab(bbox=game_coords))  # shape is [y,x]
                screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)  # convert to grey image
                shoot()

            if keyboard.is_pressed('q'):
                break

            #time.sleep(0.001)
