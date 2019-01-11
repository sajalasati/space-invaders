#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys
import time
import random
from pygame.locals import *
from main_var import *
from spaceship import *
from aliens import *
from missile import *


def add_new_alien(temp, dt):
    count = 0
    for var in alien_list:
        var.change_life(-dt)
        if var.life <= 0:
            alien_list.remove(var)
    if temp >= timeGap:
        (check, flag) = (1, 0)
        while check == 1:
            randx = random.randint(0, 7) * xx
            randy = random.randint(0, 1) * yy
            for item in alien_list:
                if item.x == randx and item.y == randy:
                    flag = 1
                    break
            if flag == 0:
                alien_list.append(Aliens(randx, randy, 1))
                check = 0
                time_start[0] = time.time()


def missile2_crash():
    for item in missile2_list:
        flagg = 0
        if item.posy < 0:
            missile2_list.remove(item)
        else:
            for var in alien_list:
                if item.posy - yy < var.y + yy:
                    if item.posx <= var.x + xx and item.posx >= var.x \
                        or item.posx + xx <= var.x + xx and item.posx \
                        + xx >= var.x:

                        # missile2_list.remove(item)

                        flagg += 1
                        var.flag_for_hit = 1
                        var.index = 2
                        var.change_life(5)
                        if var.flag_for_hit != 1:
                            global_count[0] += 1

            # to move missile up

            if time.time() - item.time >= 0.5:
                item.posy -= yy
                item.time = time.time()
        if flagg > 0:
            missile2_list.remove(item)


def missile1_crash():
    for item in missile1_list:
        if item.posy < 0:
            missile1_list.remove(item)
        else:
            for var in alien_list:
                if item.posy - yy < var.y + yy:
                    if item.posx <= var.x + xx and item.posx >= var.x \
                        or item.posx + xx <= var.x + xx and item.posx \
                        + xx >= var.x:

                        # *****************************************below line
                        # if var.flag_for_hit!=1:#means not hit by missile2
                        # else it just remains freezed

                        missile1_list.remove(item)
                        alien_list.remove(var)
                        global_count[0] += 2
                        print ('global count is ', global_count[0])

            # to move the missile up

            if time.time() - item.time >= 1:
                item.posy -= yy
                item.time = time.time()
