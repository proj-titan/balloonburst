import sys
import pygame
from random import *
from pygame.locals import *
import guibox/aguibox as GUI
pygame.init()
DISPLAYX, DISPLAYY = 640, 480
DISPLAYSURF = pygame.display.set_mode((DISPLAYX, DISPLAYY))
balloonList = []
pygame.display.set_caption('Burst Balloon!')
def randomCreate():
    x = randint(10, DISPLAYX - 10)
    y = DISPLAYY - 1
    return GUI.balloon((x, y))
def update():
	global balloonList
	DISPLAYSURF.fill((0, 0, 0))
	for looper in range(randint(1, 3)):
		balloonList.append(randomCreate())
	for looper in balloonList:
		newTransform = list(looper.transform)
		newTransform[1] += 1 # NOTE: don't del this!
		looper.setTransform(newTransform)
		looper.draw(DISPLAYSURF)
while True:
	update()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
