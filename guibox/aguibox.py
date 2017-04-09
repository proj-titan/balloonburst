import pygame
from pygame.locals import *
class balloon():
    """docstring for balloon."""
    def __init__(self, transform, img):
        self.transform = transform
        self.obj = img
        self.collider = pygame.Rect\
        ( transform[0]
        , transform[1]
        , 154
        , 200)
    #
    def draw(self, SURF):
        #pygame.draw.ellipse(SURF,
        #    (255, 255, 255),
        #    self.obj, 5)
        SURF.blit(self.obj, self.transform)
    #
    def setTransform(self, arg):
        self.transform = arg
        self.collider.topleft = arg
