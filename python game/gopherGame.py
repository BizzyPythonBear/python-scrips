import pygame
import time
import sys
from pygame import *
import simpleaudio as sa

winHeight = 500
winWidth = 500
halfWinHeight = winHeight / 2
halfWinWidth = winWidth / 2
display = (winWidth, winHeight)

gravity = 11

depth = 32
timer = pygame.time.Clock()
flags = 0
gameRunning = True
screen = pygame.display.set_mode(display, flags, depth)

jumpsfx = sa.WaveObject.from_wave_file("ya.wav")

def main():
    playerObj = playerClass(0,100)

    platformGroup = pygame.sprite.Group()
    playerGroup = pygame.sprite.Group()

    backGround = pygame.Surface((winWidth, winHeight))
    backGround.convert()
    backGround.fill(Color("#87CEEB"))

    upKey = downKey = rightKey = leftKey = False

    platformList = []
    x = y = 0
    level = ["                               ",
             "                        PPPP   ",
             "                PPPPP          ",
             "       PPPPP                   ",
             "                               ",
             "PPPPPP                         ",]
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
                if event.key == K_RIGHT:
                    rightKey = True                    
                if event.key == K_LEFT:
                    leftKey = True
                    
            if event.type == KEYUP:
                if event.key == K_UP:
                    upKey = False
                if event.key == K_DOWN:
                    downKey = False                    
                if event.key == K_RIGHT:
                    rightKey = False                   
                if event.key == K_LEFT:
                    leftKey = False                  

        screen.blit(backGround, (0,0))            
        cameraObj.update(playerObj)
        playerObj.update(upKey, downKey, leftKey, rightKey, platformList)

        for i in playerGroup:
            screen.blit(i.image, cameraObj.apply(i))
        for i in platformGroup:
            screen.blit(i.image, cameraObj.apply(i)) 
        timer.tick(60)
        pygame.display.update()

class cameraClass(object):
    def __init__(self, cameraFunc, width, height):
        self.cameraFunc = cameraFunc
        self.state = Rect(0,0,width,height)
        
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    
    def update(self, target):
        self.state = self.cameraFunc(self.state, target.rect)

def complexCamera(camera, targetRect):
    x, y, w, h = targetRect
    return Rect(halfWinWidth-x, halfWinHeight-y, w, h)
    
class entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class blockClass(entity):
    def __init__(self, x, y):
        entity.__init__(self)
        self.image = Surface((50,50))
        self.image.fill(Color("#FF0400"))
        self.image.convert()
        self.rect = Rect(x, y, 50, 50)
        
class playerClass(entity):
    def __init__(self, x, y):
        entity.__init__(self)
        self.xVel = 0
        self.yVel = 0
        self.image = Surface((50,50))
        self.image.fill(Color("#00FF33"))
        self.image.convert()
        self.rect = Rect(x, y, 50, 50)
        self.onGround = False
    def update(self, upKey, downKey, leftKey, rightKey, platforms):
        if upKey and self.onGround:
            self.yVel -= gravity
            playObj = jumpsfx.play()
        if rightKey:
            if self.xVel < 6:
                self.xVel += 1
        if leftKey:
            if self.xVel > -6:
                self.xVel -= 1
        if not (leftKey or rightKey):
            self.xVel = 0

        print(self.yVel)

        if not self.onGround and self.yVel < 100:
            self.yVel += 0.5
  
        self.rect.left += self.xVel
        self.collide(self.xVel, 0, platforms)
        self.rect.top += self.yVel
        self.onGround = False
        self.collide(0, self.yVel, platforms)

        if self.yVel > 35:
            print("Respawn!")
            playerObj(0, 100)
            
    def collide(self, xVelDelta, yVelDelta, platforms):
        for i in platforms:
            if pygame.sprite.collide_rect(self, i):
                if xVelDelta > 0:
                    self.rect.right = i.rect.left
                if xVelDelta < 0:
                    self.rect.left = i.rect.right
                if yVelDelta > 0:
                    self.rect.bottom = i.rect.top
                    self.yVel = 0
                    self.onGround = True
                if yVelDelta < 0:
                    self.rect.top = i.rect.bottom

main()


        
