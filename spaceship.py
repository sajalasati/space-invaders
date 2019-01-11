#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys
import time
import random
from pygame.locals import *
from main_var import *


class Spaceship:

    def __init__(self, index):
        '''constructor for spaceship'''

        self.index = index
        self.x = display_width / 2 - xx / 2
        self.y = display_height - 2 * yy

    def draw_img(self):
        gameDisplay.blit(img_array[self.index], (self.x, self.y))

    def changex(self, x_change):
        self.x += x_change
        if self.x > display_width - x_change:
            self.x = display_width - x_change
        elif self.x < 0:
            self.x = 0
