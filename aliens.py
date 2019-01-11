import pygame
import sys
import time
import random
from pygame.locals import *
from main_var import *


class Aliens:
    count = 0

    def __init__(self, randx, randy, index):
        "constructor for aliens"
        self.x = randx
        self.y = randy
        self.index = index
        self.life = 7
        self.flag_for_hit = 0  # hit by missile2 or not

    def draw_img(self):
        gameDisplay.blit(img_array[self.index], (self.x, self.y))

    def change_life(self, param):
        self.life += param
