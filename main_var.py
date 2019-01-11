import pygame
import sys
import time
import random
from pygame.locals import *

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
# timeDead is for auto die and timeGap is for respawn time
timeDead = 8
timeGap, display_width, display_height = 10, 720, 720

black = (0, 0, 0)
white = (255, 255, 255)
global_count = [0]

yy = 90
xx = 90

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
#######################################################

# store an array of images
img_array = [1, 2, 3, 4, 5]
img_array[0] = pygame.image.load("ship.png")
img_array[0] = pygame.transform.scale(img_array[0], (int(xx), int(yy)))
img_array[1] = pygame.image.load("a1.png")
img_array[1] = pygame.transform.scale(img_array[1], (int(xx), int(yy)))
img_array[2] = pygame.image.load("a2.png")
img_array[2] = pygame.transform.scale(img_array[2], (int(xx), int(yy)))
img_array[3] = pygame.image.load("m1.png")
img_array[3] = pygame.transform.scale(img_array[3], (int(xx), int(yy)))
img_array[4] = pygame.image.load("m2.png")
img_array[4] = pygame.transform.scale(img_array[4], (int(xx), int(yy)))

alien_list = []
missile1_list = []
missile2_list = []
time_start = []
prev_time = []
