import pygame as pg
import random
from math import *

# player class
class Player (pg.sprite.Sprite) :
    def __init__(self, xPos=0, yPos=0) :
        super().__init__()
        self.image = pg.image.load("Bilder/toolinsekt KT.png")
        self.x, self.y = xPos, yPos
        self.Bild = self.image
        self.isKilled = False   
    def rotate(self, winkel) :
        self.Bild = pg.transform.rotate(self.image, winkel)
    def move(self, Distance, xx, yy) :
        self.x += xx
        self.y += yy
        Distance -= 1
        return Distance
    def step(self, xx, yy) :
        self.x += xx
        self.y += yy
    def destroy(self) :
        self.image = pg.image.load("Bilder/toolinsekt KT.png")
        self.Bild = self.image
        self.isKilled = True
        print(self.isKilled)
        
              
# Color and controled
green = (0,255,0)
Tools = 0
xMax, yMax = 600, 400
winkel = 0
bugMax = 5
player = []
xStep = []
yStep = []
Blue = (0,0,255)

# pygame start and tools
pg.init()
pg.key.set_repeat(20,20)
pg.display.set_caption("Beetlegame")
Window = pg.display.set_mode((600, 400))


# ...

for Nr in range(0,bugMax) :
    xPos = random.randint(100,xMax-100)
    yPos = random.randint(50,yMax-100)
    player.append(Player(xPos, yPos))
for Nr in range(0,bugMax) :
    xStep.append(random.randint(0,2))
    if xStep[Nr] == 0 :
            xStep[Nr] = -1
    yStep.append(random.randint(0,2))
    if yStep[Nr] == 0 :
        yStep[Nr] = -1



# Pygame functions
running = True
while running :
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            running = False
        # Mousecontrol
        if event.type == pg.MOUSEBUTTONDOWN :
            (xPos, yPos) = pg.mouse.get_pos()
            for Nr in range(0,bugMax) :
                if (xPos > player[Nr].x) and (xPos < player[Nr].x + 100) and (yPos > player[Nr].y) and (yPos < player[Nr].y + 100) :
                    player[Nr].destroy()
                    
    # controls
    for Nr in range(0,bugMax) :
        if (player[Nr].x < 0) or (player[Nr].x > xMax-190) :
            xStep[Nr] = -xStep[Nr]
        if (player[Nr].y < 0) or (player[Nr].y > yMax-110) :
            yStep[Nr] = -yStep[Nr]
    
    # tzuiop     
        winkel = atan2(-yStep[Nr], xStep[Nr])
        winkel = degrees(winkel) - 90
        player[Nr].rotate(winkel)

        # 90789
        player[Nr].step(xStep[Nr], yStep[Nr])
        pg.time.delay(5)
            
    # The...
    Window.fill(green)
    for Nr in range(0,bugMax) :
        if not player[Nr].isKilled:
            Window.blit(player[Nr].Bild, (player[Nr].x, player[Nr].y))
    pg.display.update()
            
# EXIT pygame
pg.quit()