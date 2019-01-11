import pygame
import sys
import time
import random
from pygame.locals import *
from main_var import *


class Missile:
    def __init__(self, posx, posy):
        "missile base class"
        self.posx = posx
        self.posy = posy


class Missile1(Missile):
    def __init__(self, posx, posy, time):
        "missile1 class"
        Missile.__init__(self, posx, posy)
        self.index = 3
        self.time = time

    def draw_img(self):
        gameDisplay.blit(img_array[self.index], (self.posx, self.posy))
    # def update_y(self,)


class Missile2(Missile):
    def __init__(self, posx, posy, time):
        "missile2 class"
        Missile.__init__(self, posx, posy)
        self.index = 4
        self.time = time

    def draw_img(self):
        gameDisplay.blit(img_array[self.index], (self.posx, self.posy))
        # index = 4 will be passed
