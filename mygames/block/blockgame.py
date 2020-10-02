import pygame
import time
import sys
from pygame import *

winHeight = 500
winWidth = 500
halfWinHeight = winHeight / 2
halfWinWidth = winWidth / 2
display = (winHeight, winWidth)

gravity = 11

depth = 32
timer = pygame.time.Clock()
flags = 0
gameRunning = True
screen = pygame.display.set_mode(display, flags, depth)

def main():
    playerObj = playerClass(0, 100)

    playerGroup = pygame.sprite.Group()
    platformGroup = pygame.sprite.Group()

    backGround = pygame.Surface((winWidth, winHeight))
    backGround.convert()
    backGround.fill(Color("#87CEEB"))

    upKey = downKey = rightKey = leftKey = False

    platformList = []
    x = y = 0
    level = ["              ",
             "              ",
             "              ",
             "     PPPPP    ",
             "              ",
             "PPPPP         ",]
    for row in level:
        for col in row:
            if col == "P":
                P = blockClass(x,y)
                platformGroup.add(P)
                platformList.append(P)
            x += 50
        y += 50
        x = 0
    totalLevelWidth = len(level[0])*50
    totalLevelHeight = len(level)*50
    cameraObj = cameraClass(complexCamera, totalLevelWidth, totalLevelHeight)
    platformGroup.add(playerObj)

    while gameRunning:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    upKey = True
                if event.key == K_DOWN:
                    downKey = True
                if event.key == K_LEFT:
                    leftKey = True
                if event.key == K_RIGHT:
                    rightKey = True
                    
            if event.type == KEYUP:
                if event.key == K_UP:
                    upKey = False
                if event.key == K_DOWN:
                    downKey = False
                if event.key == K_LEFT:
                    leftKey = False
                if event.key == K_RIGHT:
                    rightKey = False
                    
        screen.blit(backGround, (0,0))
        cameraObj.update(playerObj)
        playerObj.update(upKey, downKey, leftKey, rightKey, platformList)

        for i in playerGroup:
            screen.blit(i.image, cameraObj.apply(i))
        for i in platformGroup:
            screen.blit(i.image, cameraObj.apply(i))
        timer.tick(60)
        pygame.display.update()

def cameraClass(object):
    pass

def complexCamera(camera, targetRect):
    pass
class entity():
    pass
class blockClass():
    pass
class playerClass():
    pass
