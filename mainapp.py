import sys
import pygame
import time
from random import *
from pygame.locals import *
import guibox.aguibox as GUI
pygame.init()
DISPLAYX, DISPLAYY = 640, 480
DISPLAYSURF = pygame.display.set_mode((DISPLAYX, DISPLAYY))
balloonList = []
mpos = (0, 0)
pygame.display.set_caption('Burst Balloon!')
BLIST = [ pygame.image.load('balloon.png')
        , pygame.image.load('balloon_green.png')]
gpoint = 0
FONTOBJ = pygame.font.Font('freesansbold.ttf', 32)
def randomCreate():
    x = randint(10, DISPLAYX - 164)
    y = DISPLAYY - 1
    c = randint(0, 1)
    return GUI.balloon((x, y), BLIST[c])
def update():
    global balloonList, gpoint
    DISPLAYSURF.fill((255, 255, 255))
    if randint(1,100) == 55:
        for looper in range(randint(0, 3)):
            balloonList.append(randomCreate())
    for looper in balloonList:
        newTransform = list(looper.transform)
        newTransform[1] -= 1 # NOTE: don't del this!
        looper.setTransform(newTransform)
        #looper.draw(DISPLAYSURF)
        DISPLAYSURF.blit(looper.obj, looper.transform)
    textsurf = FONTOBJ.render(str(gpoint), True, (0,0,0),(255,255,255))
    textrect = textsurf.get_rect()
    textrect.topleft = (10,10)
    DISPLAYSURF.blit(textsurf, textrect)
    for index, val in enumerate(balloonList):
        if val.collider.collidepoint(mpos):
            del balloonList[index]
            gpoint += 1
        if val.collider.y < 0:
            del balloonList[index]

while True:
    update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mpos = event.pos
    pygame.display.update()
