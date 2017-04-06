import pygame
from pygame.locals import *
class balloon():
    """docstring for balloon."""
    def __init__(self, transform):
        self.transform = transform
        self.obj = \
            pygame.rect(transform, 10,10)
    #
    def draw(self, SURF):
        pygame.draw.ellipse(SURF, 
            (255, 255, 255),
            self.obj, 5)
    #
    def setTransform(self, arg):
        self.obj.topleft = arg
        self.transform = arg
