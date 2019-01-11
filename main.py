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
from other_funcs import *


def game_loop(time_start, prev_time):

    ship = Spaceship(0)

    # add the first alien to appear at the start of game

    randx = random.randint(0, 7) * xx
    randy = random.randint(0, 1) * yy
    alien_list.append(Aliens(randx, randy, 1))
    while True:

        # to create a new alien

        temp = time.time() - time_start[0]
        dt = time.time() - prev_time[0]

        # just checks if a alien should be added or eliminated

        add_new_alien(temp,dt)

        # handling missile2

        missile2_crash()

        # handling missile1

        missile1_crash()

        # event handling of the game

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # KEYDOWN checks if a key was pressed

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit()
                if event.key == pygame.K_a:
                    ship.changex(-xx)
                if event.key == pygame.K_d:
                    ship.changex(xx)
                if event.key == pygame.K_SPACE:
                    missile1_list.append(Missile1(ship.x, ship.y - yy,
                            time.time()))
                if event.key == pygame.K_s:
                    missile2_list.append(Missile2(ship.x, ship.y - yy,
                            time.time()))

        # draw following onto the pygame window

        textsurface = myfont.render('Score: ' + str(global_count[0]),
                                    False, (0, 0, 0))

        gameDisplay.fill(white)
        gameDisplay.blit(textsurface, (300, 640))
        ship.draw_img()
        for i in range(0, len(alien_list)):
            alien_list[i].draw_img()
        for i in range(0, len(missile1_list)):
            missile1_list[i].draw_img()
        pygame.display.update()
        for i in range(0, len(missile2_list)):
            missile2_list[i].draw_img()
        pygame.display.update()
        prev_time[0] = time.time()

        # till here

        clock.tick(60)


time_start.append(time.time())
prev_time.append(time.time())
game_loop(time_start, prev_time)

pygame.quit()
sys.exit()