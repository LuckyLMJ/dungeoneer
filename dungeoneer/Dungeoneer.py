# Dungeon Dash

import pygame, sys, random, time
from pygame.locals import *



pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

Xbox = False

pygame.display.set_caption('Dungeoneer')

treasure = [0,0]

tiles1 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,2,5,7,5,6,7,1,5,13,14,16,14,5,7,1,0,17,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,17,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,5,6,0,0,0,2,1,15,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,4,0,0,13,16,0,0,0,0,0,0,0,0,1,2,0,19,0,19,0,0,0,0,6,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,7,4,0,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0,1,0,1,5,6,7,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0,1,1,1,0,1,8,3,8,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,23,17,22,0,1,0,0,0,1,0,1,4,0,19,0,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,2,0,1,0,1,1,1,1,1,1,1,1,8,0,0,0,8,1,1,0,1,6,5,1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,22,0,22,0,1,0,0,0,1,0,1,6,7,5,1,8,0,0,0,0,0,0,0,0,0,0,1,0,7,1,2,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,5,1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,22,0,23,0,1,1,1,1,1,1,1,1,1,1,1,8,0,0,0,0,0,0,0,0,0,0,1,0,7,1,1,1,1,0,1,11,11,11,1,0,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,8,0,0,0,8,1,1,0,1,5,2,1,17,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,22,17,22,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,11,10,11,10,11,10,11,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,14,24,0,0,23,1,0,0,0,1,0,1,1,0,0,0,1,1,1,0,1,10,11,10,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,2,17,2,17,2,0,1,0,0,0,0,0,0,0,2,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,17,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,23,0,5,7,23,1,0,0,0,1,17,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,2,17,2,17,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,9,9,1,9,2,6,1,9,8,9,1,9,9,17,1,9,6,9,2,9,8,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


tiles2 = [[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1,17,25,17,25,17, 1,26, 1, 6, 7, 5, 6, 2, 1, 1,14,16,14,13, 7, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 5, 2, 0, 7, 5, 1, 1, 0, 0, 0, 0, 5, 1, 1,29, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1,25,25, 0,25,25, 1,19, 1, 0, 0, 4, 0,16, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 2,17, 2, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0,28,16,15, 7, 1, 1, 0, 1,17,26,17, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 0, 0, 0, 1,25,25, 0,25,25, 1,19, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,19, 0,19, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 0,29, 0, 0, 0,29, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 2, 2, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 8,30,30, 0, 8,30, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 0, 1, 0,17, 1, 1, 5, 7, 0, 1, 4, 1, 1, 0,26, 0, 1, 1, 0, 1,17, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 0, 0, 0,26, 1, 1, 6, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1,29, 1, 1, 1,25,25, 0,25, 1,11, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 0,17, 1, 1, 0, 0, 0, 1,19, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1, 0, 0, 0,19, 0, 1, 2, 7, 6, 5, 7, 1, 0, 1, 1, 0, 0, 0, 1,25,25, 0,17, 1,11, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 5, 0, 0, 0, 5, 1, 0, 1, 1,17,26,17, 1, 0, 0, 0, 0, 1, 1, 1,30, 0, 0, 0, 0, 0, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1,25,25, 0,25, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1,19, 1,31, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1, 0, 1, 0, 9, 7, 9,17, 9, 0, 1, 0, 5, 9, 8, 9, 0, 1, 5, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 7, 5, 0, 0, 6, 1, 1,19, 1, 0, 0, 0, 1, 1, 0, 0,33,11,14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1,17, 1, 6, 9, 8, 9, 2, 9, 5, 1, 9,17, 9, 7, 9,26, 1, 6, 2, 6, 7, 5, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,19, 1, 1, 0, 0, 0,31, 0, 0, 0, 0,16, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 2, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,15, 0,32,32,28, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

leveli = []
level = []

for t in range(0, 50):
    level.append(leveli)

for i in range(0, 50):
    for y in range(0, 50):
        level[i].append(0)
        
for i in range(0, 50):
    for y in range(0, 50):
       level[i][y] = 0
            
'''
for q in range(0, 10):
    randi = random.randint(5, 35)
    randy = random.randint(5, 35)
    for i in range(0, 9):
        for y in range(0, 9):
            level[randi + i][randy + y] = 0'''



TILES = [tiles1, tiles2]
Rand = 1
tiles = TILES[Rand]

for p in range(0, len(tiles)):
    for o in range(0, len(tiles[p])):
        if tiles[p][o] == 17:
            if random.randint(0, 2) == 1:
                tiles[p][o] = 18
           
Tiles = []
BadGuys = []

inventory = []


sp = 0
SP = [[10,-20],[-400,-320],[-700,-220],[-1200,-220]]
TP = [[-20,-480],[-700,-480],[-224,72],[130,-280],[-526,-26],[-678,116],[-674,-174],[-776,-340]]
Y = SP[sp][1]
X = SP[sp][0]
LX = X
LY = Y





MOVELEFT = False
MOVERIGHT = False
MOVEUP = False
MOVEDOWN = False

Attack = False
AttackCD = 0
AttackI = -1

Brake = False
BrakeT = 0

TT = False



MOVESPEED = 2

TreasureL = [[-280,126],[-624,-126],[-378,-280],[-478,-676],[-218,-424],[72,-374]]


CrateLT = [0,0,0,8,8,9,9,9,7,7,7,1,1,1,1,2,9,9,8,8,6,1,1,1,1,0,2,4]
ChestLT = [0,0,0,0,0,1,1,1,1,1,2,1,1,1,1,2,2,0,0,0,4,4,6]
GChestLT = [0,0,1,1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,4,5,6,6]


mousex, mousey = pygame.mouse.get_pos()
if Xbox == False:
    mouseRect = pygame.Rect(mousex,mousey,5,5)
else:
    mX = 450
    mY = 250
    mouseRect = pygame.Rect(mX,mY,5,5)
mouseI = pygame.image.load('Mouse.png')
MouseSI = pygame.transform.scale(mouseI, (20, 20))


BrakeR = pygame.Rect(mousex, mousey, BrakeT, 3)
    
Icon = pygame.image.load('Icon.png')
pygame.display.set_icon(Icon)

pygame.joystick.init()

joystick_count = pygame.joystick.get_count()


Trap = False
TrapT = 0

BadGuyA = 5

Lives = 5
HCD = 0

HeartI = [pygame.image.load('Heart.png'), pygame.image.load('BHeart.png')]
hearts = []
Items = []
basicFont = pygame.font.SysFont(None, 20)

class HEART(object):
    def __init__(self,x,y,Lives,HeartI,HN):
        self.x = x
        self.y = y
        self.I = pygame.image.load('Heart.png')
        self.N = HN
        self.SI = pygame.transform.scale(self.I, (40, 40))
        self.R = pygame.Rect(self.x, self.y, 40,40)
    def draw(self,windowSurface):
        windowSurface.blit(self.SI, self.R)
class INVENTORY(object):
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.N = num
        self.T = 0
        self.E = True
        self.A = 0
        self.S = False
        self.SS = False
        self.TL = [0,0]
        self.I = pygame.image.load('Empty.png')
        self.SI = pygame.transform.scale(self.I, (50,50))
        self.R = pygame.Rect(self.x, self.y, 50, 50)
        self.TE = basicFont.render(str(self.A), True, (50,50,50))
        self.TR = self.TE.get_rect()
        self.TR.centerx = (self.x + 40)
        self.TR.centery = (self.y + 40)

    def draw(self,windowSurface):
        if Slot.S == False:
            windowSurface.blit(self.SI, self.R)
        else:
            windowSurface.blit(self.SI, (self.R.x - 5, self.R.y - 5))   
        if self.A != 0:
            windowSurface.blit(self.TE, self.TR)

Coin = pygame.image.load('CoinS.png')
Key = pygame.image.load('KeyS.png')
Orb = pygame.image.load('OrbSlot.png')
TOrb = pygame.image.load('TOrbSlot.png')
Empty = pygame.image.load('Empty.png')
FireP = pygame.image.load('FirePendantS.png')
Compass = pygame.image.load('CompassSlot.png')
IronSwordS = pygame.image.load('IronSwordS.png')
BoneSwordS = pygame.image.load('BoneSwordS.png')
Spear = pygame.image.load('SpearS.png')

Slots = []
SlotI = [Empty,Coin,Key,Orb,TOrb,FireP,Compass,IronSwordS,BoneSwordS,Spear]

TOP = pygame.Rect(0,0,1000,100)
BOTTOM = pygame.Rect(0,500,1000,100)
RIGHT = pygame.Rect(0,0,300,600)
LEFT = pygame.Rect(700,0,300,600)
MIDDLE = pygame.Rect(300,100,400,400)
MIDDLEI = pygame.image.load('Dark.png')
MIDDLESI = pygame.transform.scale(MIDDLEI,(400, 400))
HR = pygame.Rect(10, 10, 280, 550)

Floor = pygame.image.load('WallTile.png')
Wall = pygame.image.load('FloorTile.png')
Fountain = pygame.image.load('FountainTile.png')
LChest = pygame.image.load('LChestTile.png')
LGChest = pygame.image.load('LGChestTile.png')
CLever = pygame.image.load('CLeverTile.png')
OLever = pygame.image.load('OLeverTile.png')
Crate1 = pygame.image.load('CrateTile.png')
Crate2 = pygame.image.load('CrateTile2.png')
Crate3 = pygame.image.load('CrateTile3.png')
Plant = pygame.image.load('PlantTile.png')
Plant2 = pygame.image.load('PlantTile2.png')
Bed = pygame.image.load('BedTile.png')
WR = pygame.image.load('WeaponRackTile.png')
AR = pygame.image.load('ArmourRackTile.png')
Anvil = pygame.image.load('AnvilTile.png')
Oven = pygame.image.load('OvenTile.png')
GrindStone = pygame.image.load('GrindStoneTile.png')
SmithTable = pygame.image.load('SmithingTableTile.png')
OrbT = pygame.image.load('OrbTile.png')
Orb = pygame.image.load('OrbHolderTile.png')
NTrap = pygame.image.load('TrapTile.png')
ETrap = pygame.image.load('ETrapTile.png')
OChest = pygame.image.load('UChestTile.png')
OGChest = pygame.image.load('UGChestTile.png')
Table = pygame.image.load('TableTile.png')
Counter = pygame.image.load('CounterTile.png')
Spit = pygame.image.load('SpitTile.png')
Book = pygame.image.load('BookShelfTile.png')
TRack = pygame.image.load('ToolRackTile.png')
Lock = pygame.image.load('LockTile.png')
Crack = pygame.image.load('CrackedTile.png')
Desk = pygame.image.load('DeskTile.png')
Shelf = pygame.image.load('ShelfTile.png')

PR = pygame.image.load('PlayerRight.png')
PR1 = pygame.image.load('PlayerRight1.png')
PR2 = pygame.image.load('PlayerRight2.png')
PL = pygame.image.load('PlayerLeft.png')
PL1 = pygame.image.load('PlayerLeft1.png')
PL2 = pygame.image.load('PlayerLeft2.png')
PD = pygame.image.load('PlayerDown.png')
PD1 = pygame.image.load('PlayerDown1.png')
PD2 = pygame.image.load('PlayerDown2.png')
PU = pygame.image.load('PlayerUp.png')
PU1 = pygame.image.load('PlayerUp1.png')
PU2 = pygame.image.load('PlayerUp2.png')

E1R = pygame.image.load('DwarfGaurdRight.png')
E1R1 = pygame.image.load('DwarfGaurdRight1.png')
E1R2 = pygame.image.load('DwarfGaurdRight2.png')
E1L = pygame.image.load('DwarfGaurdLeft.png')
E1L1 = pygame.image.load('DwarfGaurdLeft1.png')
E1L2 = pygame.image.load('DwarfGaurdLeft2.png')
E1D = pygame.image.load('DwarfGaurdDown.png')
E1D1 = pygame.image.load('DwarfGaurdDown1.png')
E1D2 = pygame.image.load('DwarfGaurdDown2.png')
E1U = pygame.image.load('DwarfGaurdUp.png')
E1U1 = pygame.image.load('DwarfGaurdUp1.png')
E1U2 = pygame.image.load('DwarfGaurdUp2.png')

E2R = pygame.image.load('DwarfGaurd2Right.png')
E2R1 = pygame.image.load('DwarfGaurd2Right1.png')
E2R2 = pygame.image.load('DwarfGaurd2Right2.png')
E2L = pygame.image.load('DwarfGaurd2Left.png')
E2L1 = pygame.image.load('DwarfGaurd2Left1.png')
E2L2 = pygame.image.load('DwarfGaurd2Left2.png')
E2D = pygame.image.load('DwarfGaurd2Down.png')
E2D1 = pygame.image.load('DwarfGaurd2Down1.png')
E2D2 = pygame.image.load('DwarfGaurd2Down2.png')
E2U = pygame.image.load('DwarfGaurd2Up.png')
E2U1 = pygame.image.load('DwarfGaurd2Up1.png')
E2U2 = pygame.image.load('DwarfGaurd2Up2.png')



M = pygame.image.load('Mouse.png')

UAI = pygame.image.load('UpArrow.png')
UASI = pygame.transform.scale(UAI,(50,50))

DAI = pygame.image.load('DownArrow.png')
DASI = pygame.transform.scale(DAI,(50,50))

RAI = pygame.image.load('RightArrow.png')
RASI = pygame.transform.scale(RAI,(50,50))

LAI = pygame.image.load('LeftArrow.png')
LASI = pygame.transform.scale(LAI,(50,50))


player = pygame.Rect(485, 285, 30, 30)
playerI = playerI = pygame.image.load('PlayerRight.png')
playerSI = pygame.transform.scale(playerI, (80, 80))
PlayerI = pygame.Rect(450, 250, 100, 100)
PlayerA = pygame.Rect(440, 240, 120, 120)

NoMoveTiles = [1,2,3,5,6,7,9,10,11,13,14,15,16,18,21,22,23,25,26,27,28,29]
Stackable = [1,3,4]
Weapons = [7,8,9]

WalkR = [PR,PR,PR,PR,PR1,PR1,PR1,PR1,PR,PR,PR,PR,PR2,PR2,PR2,PR2]
WalkL = [PL,PL,PL,PL,PL1,PL1,PL1,PL1,PL,PL,PL,PL,PL2,PL2,PL2,PL2]
WalkD = [PD,PD,PD,PD,PD1,PD1,PD1,PD1,PD,PD,PD,PD,PD2,PD2,PD2,PD2]
WalkU = [PU,PU,PU,PU,PU1,PU1,PU1,PU1,PU,PU,PU,PU,PU2,PU2,PU2,PU2]

E1WalkR = [E1R,E1R,E1R,E1R,E1R1,E1R1,E1R1,E1R1,E1R,E1R,E1R,E1R,E1R2,E1R2,E1R2,E1R2]
E1WalkL = [E1L,E1L,E1L,E1L,E1L1,E1L1,E1L1,E1L1,E1L,E1L,E1L,E1L,E1L2,E1L2,E1L2,E1L2]
E1WalkD = [E1D,E1D,E1D,E1D,E1D1,E1D1,E1D1,E1D1,E1D,E1D,E1D,E1D,E1D2,E1D2,E1D2,E1D2]
E1WalkU = [E1U,E1U,E1U,E1U,E1U1,E1U1,E1U1,E1U1,E1U,E1U,E1U,E1U,E1U2,E1U2,E1U2,E1U2]

E2WalkR = [E2R,E2R,E2R,E2R,E2R1,E2R1,E2R1,E2R1,E2R,E2R,E2R,E2R,E2R2,E2R2,E2R2,E2R2]
E2WalkL = [E2L,E2L,E2L,E2L,E2L1,E2L1,E2L1,E2L1,E2L,E2L,E2L,E2L,E2L2,E2L2,E2L2,E2L2]
E2WalkD = [E2D,E2D,E2D,E2D,E2D1,E2D1,E2D1,E2D1,E2D,E2D,E2D,E2D,E2D2,E2D2,E2D2,E2D2]
E2WalkU = [E2U,E2U,E2U,E2U,E2U1,E2U1,E2U1,E2U1,E2U,E2U,E2U,E2U,E2U2,E2U2,E2U2,E2U2]


USECD = 0

SH = 0

WeaponR = (0,0,0,0)


class TILE(object):
    def __init__(self,x,y,X,Y,tile,i,q):
        self.x = x + X
        self.y = y + Y
        self.X = x 
        self.Y = y
        self.i = i
        self.q = q
        self.R = pygame.Rect(self.x, self.y, 50, 50)
        self.T = tile
        if self.T == 0:
            self.I = pygame.image.load('WallTile.png')
        elif self.T == 1:
            self.I = pygame.image.load('FloorTile.png')
        elif self.T == 2:
            self.I = pygame.image.load('LChestTile.png')
            self.O = False
        elif self.T == 3:
            self.I = pygame.image.load('FountainTile.png')
        elif self.T == 4:
            self.I = pygame.image.load('CLeverTile.png')
        elif self.T == 5:
            self.I = pygame.image.load('CrateTile.png')
            self.O = False
        elif self.T == 6:
            self.I = pygame.image.load('CrateTile2.png')
            self.O = False
        elif self.T == 7:
            self.I = pygame.image.load('CrateTile3.png')
            self.O = False
        elif self.T == 8:
            self.I = pygame.image.load('PlantTile.png')
        elif self.T == 9:
            self.I = pygame.image.load('BedTile.png')
        elif self.T == 10:
            self.I = pygame.image.load('WeaponRackTile.png')
        elif self.T == 11:
            self.I = pygame.image.load('ArmourRackTile.png')
        elif self.T == 12:
            self.I = pygame.image.load('OLeverTile.png')
        elif self.T == 13:
            self.I = pygame.image.load('AnvilTile.png')
        elif self.T == 14:
            self.I = pygame.image.load('OvenTile.png')
        elif self.T == 15:
            self.I = pygame.image.load('GrindStoneTile.png')
        elif self.T == 16:
            self.I = pygame.image.load('SmithingTableTile.png')
        elif self.T == 17:
            self.I = pygame.image.load('OrbTile.png')
        elif self.T == 18:
            self.I = pygame.image.load('OrbHolderTile.png')
        elif self.T == 19:
            self.I = pygame.image.load('TrapTile.png')
        elif self.T == 20:
            self.I = pygame.image.load('ETrapTile.png')
        elif self.T == 21:
            self.I = pygame.image.load('UChestTile.png')
        elif self.T == 22:
            self.I = pygame.image.load('TableTile.png')
        elif self.T == 23:
            self.I = pygame.image.load('CounterTile.png')
        elif self.T == 24:
            self.I = pygame.image.load('SpitTile.png')
        elif self.T == 25:
            self.I = pygame.image.load('BookShelfTile.png')
        elif self.T == 26:
            self.I = pygame.image.load('LGChestTile.png')
        elif self.T == 27:
            self.I = pygame.image.load('UGChestTile.png')
        elif self.T == 28:
            self.I = pygame.image.load('ToolRackTile.png')
        elif self.T == 29:
            self.I = pygame.image.load('LockTile.png')
        elif self.T == 30:
            self.I = pygame.image.load('PlantTile2.png')
        elif self.T == 31:
            self.I = pygame.image.load('CrackedTile.png')
        elif self.T == 32:
            self.I = pygame.image.load('DeskTile.png')
        elif self.T == 33:
            self.I = pygame.image.load('ShelfTile.png')
        
            
        self.SI = pygame.transform.scale(self.I, (50, 50))
    def draw(self,windowSurface):
        windowSurface.blit(self.SI, self.R)
        
class BADGUY(object):
    def __init__(self,X,Y,x,y):
        self.x = x
        self.y = y
        self.lx = x
        self.ly = y
        self.X = x
        self.Y = y
        self.L = 5
        self.i = 0
        self.C = (0,255,0)
        self.rect = pygame.Rect(self.x, self.y, 30, 35)
        self.I = pygame.image.load('E1Right.png')
        self.SI = pygame.transform.scale(self.I, (60,60))
    def draw(self,windowSurface):
        for BadGuy in BadGuys:
            #pygame.draw.rect(windowSurface, self.C, self.rect)
            windowSurface.blit(self.SI, self.rect)
            
class ITEM(object):
    def __init__(self,X,Y,x,y,ItemT,TL):
        self.x = x + X
        self.y = y + Y
        self.X = x + X
        self.Y = y + Y
        self.T = ItemT
        self.TL = TL
        if ItemT == 1:
            self.I = pygame.image.load('Coin.png')
        if ItemT == 2:
            self.I = pygame.image.load('Key.png')
        if ItemT == 3:
            self.I = pygame.image.load('OrbI.png')
        if ItemT == 4:
            self.I = pygame.image.load('TeleOrbI.png')
        if ItemT == 5:
            self.I = pygame.image.load('FirePendantI.png')
        if ItemT == 6:
            self.I = pygame.image.load('Compass.png')
        if ItemT == 7:
            self.I = pygame.image.load('IronSwordI.png')
        if ItemT == 8:
            self.I = pygame.image.load('BoneSwordI.png')
        if ItemT == 9:
            self.I = pygame.image.load('SpearI.png')
        self.SI = pygame.transform.scale(self.I, (20, 20))
        self.R = pygame.Rect(self.x, self.y, 20, 20)
    def draw(self,windowSurface):
        for Item in Items:
            #pygame.draw.rect(windowSurface, (255,0,0), self.R)
            windowSurface.blit(self.SI, self.R)
            



            
for i in range(0, 12):
    for q in range(0, 20):
        x = q * 50
        y = i * 50
        tile = tiles[i][q]
        Tiles.append(TILE(x,y,X,Y,tile,i,q))
        
for r in range(0, Lives):
    if r > 4:
        y = 50
        R = r - 5
        x = R * 50 + 25
    else:
        y = 10
        x = r * 50 + 25
   
    HN = r 
    hearts.append(HEART(x,y,Lives,HeartI,HN))

for r in range(0,6):
    for t in range(0,4):
        x = t * 70 + 20
        y = r * 70 + 150
        num = r * t
        Slots.append(INVENTORY(x,y,num))
    
Image = 0

pygame.mouse.set_visible(False)
        

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
        if event.type == KEYDOWN and Xbox == False:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_a:
                MOVELEFT = True
                MOVERIGHT = False
                playerI = WalkL[0]
            if event.key == K_d:
                MOVERIGHT = True
                MOVELEFT = False
                playerI = WalkR[0]
            if event.key == K_s:
                MOVEDOWN = True
                MOVEUP = False
                playerI = WalkD[0]
            if event.key == K_w:
                MOVEUP = True
                MOVEDOWN = False
                playerI = WalkU[0]
        if event.type == KEYUP and Xbox == False:
            if event.key == K_a:
                MOVELEFT = False
                playerI = PL
            if event.key == K_d:
                MOVERIGHT = False
                playerI = PR
            if event.key == K_s:
                MOVEDOWN = False
                playerI = PD
            if event.key == K_w:
                MOVEUP = False
                playerI = PU
                
        if Xbox == True:
            for i in range(joystick_count):
                joystick = pygame.joystick.Joystick(i)
                joystick.init()
                
                axes = joystick.get_numaxes()
                
                for i in range(axes):
                    axis = round(joystick.get_axis(i))
                    if i == 3:
                        print(axis)
                    if i == 4 and axis == -1:
                        MX = -1
                    elif i == 4 and axis == 1:
                        MX = 1
                    else:
                        MX = 0
                    if i == 3 and axis == -1:
                        MY = -1
                    elif i == 3 and axis == 1:
                        MY = 1
                    else:
                        if i == 3:
                            MY = 0
                    
                    
                    axis = round(joystick.get_axis(i))
                    
                    if i == 0 and axis == 1:
                        MOVERIGHT = True
                        MOVELEFT = False
                        #playerI = WalkL[0]
                    elif i == 0 and axis == -1:
                        MOVELEFT = True
                        MOVERIGHT = False
                        #playerI = WalkR[0]
                    if i == 1 and axis == 1:
                        MOVEDOWN = True
                        MOVEUP = False
                        #playerI = WalkD[0]
                    elif i == 1 and axis == -1:
                        MOVEUP = True
                        MOVEDOWN = False
                        #playerI = WalkU[0]
                    if i == 0 and axis == 0:
                        MOVELEFT = False
                        MOVERIGHT = False
                    if i == 1 and axis == 0:
                        MOVEUP = False
                        MOVEDOWN = False
                    
                    
                    
            
                buttons = joystick.get_numbuttons()
                
                for i in range(buttons):
                    button = joystick.get_button(i)
            
                    if i == 0 and button == 1:
                        MOSI = True
                    else:
                        if i == 0:
                            MOSI = False
                    if i == 1 and button == 1:
                        MOSQ = True
                    else:
                        if i == 1:
                            MOSQ = False
    
    windowSurface.fill(BLACK)
    
    
    TrapT += .9
    if TrapT > 50:
        TrapT = 0
        if Trap == True:
            Trap = False
            for Tile in Tiles:
                if Tile.T == 20:
                    Tile.T = 19
                    try:
                        tiles[Tile.i][Tile.q] = 19
                    except:
                        pass
                        
        else:
            Trap = True
            for Tile in Tiles:
                if Tile.T == 19:
                    Tile.T = 20
                    try:
                        tiles[Tile.i][Tile.q] = 20
                    except:
                        pass

            
    
    for BadGuy in BadGuys:
        BadGuy.x = BadGuy.X + X
        BadGuy.y = BadGuy.Y + Y
        if BadGuy.x > 50 and BadGuy.x < WINDOWWIDTH - 50 and BadGuy.y > 50 and BadGuy.y < WINDOWHEIGHT - 50:
            if player.x > BadGuy.x:
                BadR = pygame.Rect(BadGuy.x, BadGuy.y, 45,30)
                Go = True
                for Tile in Tiles:
                    if Tile.R.colliderect(BadR) and Tile.T in NoMoveTiles:
                        Go = False
                if Go == True:
                    BadGuy.i += 1
                    if BadGuy.i >= len(E1WalkR):
                        BadGuy.i = 0
                    BadGuy.I = E1WalkR[BadGuy.i]
                    BadGuy.X += 1
                    hit = False
                    BadGuy.rect = pygame.Rect(BadGuy.x, BadGuy.y, 30, 35)
                    for Tile in Tiles:
                        if Tile.R.colliderect(BadGuy.rect) and Tile.T == 1:
                            hit = True
                    if hit == True:
                        BadGuy.X = BadGuy.lx - 5
            if player.x < BadGuy.x:
                BadR = pygame.Rect(BadGuy.x - 10, BadGuy.y, 45,30)
                Go = True
                for Tile in Tiles:
                    if Tile.R.colliderect(BadR) and Tile.T in NoMoveTiles:
                        Go = False
                if Go == True:
                    BadGuy.i += 1
                    if BadGuy.i >= len(E1WalkL):
                        BadGuy.i = 0
                    BadGuy.I = E1WalkL[BadGuy.i]
                    BadGuy.X -= 1
                    hit = False
                    BadGuy.rect = pygame.Rect(BadGuy.x, BadGuy.y, 30, 35)
                    for Tile in Tiles:
                        if Tile.R.colliderect(BadGuy.rect) and Tile.T == 1:
                            hit = True
                    if hit == True:
                        BadGuy.X = BadGuy.lx 
            if player.y > BadGuy.y:
                BadR = pygame.Rect(BadGuy.x, BadGuy.y, 30,45)
                Go = True
                for Tile in Tiles:
                    if Tile.R.colliderect(BadR) and Tile.T in NoMoveTiles:
                        Go = False
                if Go == True:
                    BadGuy.i += 1
                    if BadGuy.i >= len(E1WalkD):
                        BadGuy.i = 0
                    BadGuy.I = E1WalkD[BadGuy.i]
                    BadGuy.Y += 1
                    hit = False
                    BadGuy.rect = pygame.Rect(BadGuy.x, BadGuy.y, 30, 35)
                    for Tile in Tiles:
                        if Tile.R.colliderect(BadGuy.rect) and Tile.T == 1:
                            hit = True
                    if hit == True:
                        BadGuy.Y = BadGuy.ly 
            if player.y < BadGuy.y:
                BadR = pygame.Rect(BadGuy.x, BadGuy.y - 10, 30,45)
                Go = True
                for Tile in Tiles:
                    if Tile.R.colliderect(BadR) and Tile.T in NoMoveTiles:
                        Go = False
                if Go == True:
                    if BadGuy.i >= len(E1WalkU):
                        BadGuy.i = 0
                    BadGuy.I = E1WalkU[BadGuy.i]
                    BadGuy.Y -= 1
                    hit = False
                    BadGuy.rect = pygame.Rect(BadGuy.x, BadGuy.y, 30, 35)
                    for Tile in Tiles:
                        if Tile.R.colliderect(BadGuy.rect) and Tile.T == 1:
                            hit = True
                    if hit == True:
                        BadGuy.Y = BadGuy.ly
          
        
        
        BadGuy.x = BadGuy.X + X
        BadGuy.y = BadGuy.Y + Y
        
        hit = False
        for Tile in Tiles:
            if Tile.R.colliderect(BadGuy.rect) and Tile.T == 1:
                hit = True
        if hit == True:
            BadGuy.Y = BadGuy.ly
            BadGuy.X = BadGuy.lx
        
        BadGuy.SI = pygame.transform.scale(BadGuy.I, (60,60))
        #BadGuy.lx = BadGuy.X
        #BadGuy.ly = BadGuy.Y
        BadGuy.rect = pygame.Rect(BadGuy.x, BadGuy.y, 30, 35)
        #if BadGuy.x > 377 and BadGuy.x < 585 and BadGuy.y > 215 and BadGuy.y < 425:
        BadGuy.draw(windowSurface)
        
    
    for BadGuy in BadGuys:
        BadGuy.x = BadGuy.X + X
        BadGuy.y = BadGuy.Y + Y
        BadGuy.rect = pygame.Rect(BadGuy.x, BadGuy.y, 30, 35)
        hit = False
        for Tile in Tiles:
            if Tile.R.colliderect(BadGuy.rect) and Tile.T == 1:
                hit = True
        if hit == False:
            BadGuy.lx = BadGuy.X 
            BadGuy.ly = BadGuy.Y
        
        if BadGuy.rect.colliderect(player):
            if HCD < 0:
                Lives -= 1
                HCD = 20
                
        if BadGuy.rect.colliderect(WeaponR) and Attack == True:
            Attack = True
            BadGuy.L -= 1
            if BadGuy.L < 1:
                BadGuys.pop(BadGuys.index(BadGuy))
    
    if Xbox == False:
        mousex, mousey = pygame.mouse.get_pos()
        mouseRect = pygame.Rect(mousex,mousey,20,20)
    else:
        print(MY)
        if MX == -1:
            mX -= 4
        elif MX == 1:
            mX += 4
        if MY == -1:
            mY -= 4
        elif MY == 1:
            mY += 4
        mouseRect = pygame.Rect(mX,mY,20,20)
    mouseI = pygame.image.load('Mouse.png')
    MouseSI = pygame.transform.scale(mouseI, (20, 20))
    
    
    
       
    playerSI = pygame.transform.scale(playerI, (60, 60))
    
    
    if MOVEDOWN == True:
        Image += 1
        if Image >= len(WalkD):
            Image = 0
        playerI = WalkD[Image]
        Y -= MOVESPEED
        Hit = False
        for Tile in Tiles:
            Tile.R = pygame.Rect(Tile.x, Tile.y, 50, 50)
            if Tile.R.colliderect(player) and Tile.T in NoMoveTiles:
                Hit = True
        if Hit == True:
            Y = LY
            MOVEDOWN = False
        else:
            LY = Y + MOVESPEED 
        
    if MOVEUP == True:
        Image += 1
        if Image >= len(WalkU):
            Image = 0
        playerI = WalkU[Image]
        Y += MOVESPEED
        Hit = False
        for Tile in Tiles:
            Tile.R = pygame.Rect(Tile.x, Tile.y, 50, 50)
            if Tile.R.colliderect(player) and Tile.T in NoMoveTiles:
                Hit = True
        if Hit == True:
            Y = LY
            MOVEUP = False
        else:
            LY = Y - MOVESPEED 
        
    if MOVERIGHT == True:
        Image += 1
        if Image >= len(WalkR):
            Image = 0
        playerI = WalkR[Image]
        X -= MOVESPEED
        Hit = False
        for Tile in Tiles:
            Tile.R = pygame.Rect(Tile.x, Tile.y, 50, 50)
            if Tile.R.colliderect(player) and Tile.T in NoMoveTiles:
                Hit = True
        if Hit == True:
            X = LX
            MOVERIGHT = False
        else:
            LX = X + MOVESPEED 
        
    if MOVELEFT == True:
        Image += 1
        if Image >= len(WalkL):
            Image = 0
        playerI = WalkL[Image]
        X += MOVESPEED
        Hit = False
        for Tile in Tiles:
            Tile.R = pygame.Rect(Tile.x, Tile.y, 50, 50)
            if Tile.R.colliderect(player) and Tile.T in NoMoveTiles:
                Hit = True
        if Hit == True:
            X = LX
            MOVELEFT = False
        else:
            LX = X - MOVESPEED
            
    
    for Tile in Tiles:
        if Tile.R.colliderect(player) and Tile.T in NoMoveTiles:
            X = LX
            Y = LY
    
    
        

    Up = False
    Down = False
    Right = False
    Left = False
    
    
    
    for Tile in Tiles:
        Tile.x = X + Tile.X
        Tile.y = Y + Tile.Y
        Tile.R = pygame.Rect(Tile.x, Tile.y, 50, 50)
        if Tile.x < 0:
            Tile.X += 1000
            Tile.q += 20
            try:
                Tile.T = tiles[Tile.i][Tile.q]
            except:
                Tile.T == 1
            if Tile.T == 0:
                if len(BadGuys) < 8:
                    if random.randint(0, 100) == 1:
                        x = Tile.X
                        y = Tile.Y 
                        BadGuys.append(BADGUY(X,Y,x,y))
        if Tile.x > 1000:
            Tile.X -= 1000
            Tile.q -= 20
            try:
                Tile.T = tiles[Tile.i][Tile.q]
            except:
                Tile.T == 1
            if Tile.T == 0:
                if len(BadGuys) < 8:
                    if random.randint(0, 100) == 1:
                        x = Tile.X 
                        y = Tile.Y 
                        BadGuys.append(BADGUY(X,Y,x,y))
        if Tile.y < 0:
            Tile.Y += 600
            Tile.i += 12
            try:
                Tile.T = tiles[Tile.i][Tile.q]
            except:
                Tile.T == 1
            if Tile.T == 0:
                if len(BadGuys) < 8:
                    if random.randint(0, 100) == 1:
                        x = Tile.X
                        y = Tile.Y 
                        BadGuys.append(BADGUY(X,Y,x,y))
        if Tile.y > 600:
            Tile.Y -= 600
            Tile.i -= 12
            try:
                Tile.T = tiles[Tile.i][Tile.q]
            except:
                Tile.T == 1
            if Tile.T == 0:
                if len(BadGuys) < 8:
                    if random.randint(0, 100) == 1:
                        x = Tile.X
                        y = Tile.Y
                        BadGuys.append(BADGUY(X,Y,x,y))
        if Xbox == False:
            if Tile.R.colliderect(mouseRect) and Tile.R.colliderect(PlayerI) and Tile.i == 3 and Tile.q == 16 and Tile.T == 4 and event.type == MOUSEBUTTONDOWN and event.button == 1:
                tiles[18][27] = 0
                tiles[Tile.i][Tile.q] = 12
                Tile.T = tiles[Tile.i][Tile.q]
            if Tile.R.colliderect(mouseRect) and Tile.R.colliderect(PlayerI) and Tile.T == 18 and event.type == MOUSEBUTTONDOWN and event.button == 1:
                tiles[Tile.i][Tile.q] = 17
                Tile.T = tiles[Tile.i][Tile.q]
                x = Tile.x - X - X + 5 + random.randint(-5, 5)
                y = Tile.y - Y - Y + 5 + random.randint(-5, 5)
                ItemT = 3
                TL = [0,0]
                Items.append(ITEM(X,Y,x,y,ItemT,TL))
                        
            if Tile.R.colliderect(mouseRect) and Tile.R.colliderect(PlayerI) and Tile.T == 2 and event.type == MOUSEBUTTONDOWN and event.button == 1:
                if Brake == False:
                    Brake = True
                    BrakeT = 50
                    Bi = Tile.i
                    Bq = Tile.q
            if Tile.R.colliderect(mouseRect) and Tile.R.colliderect(PlayerI) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                if Tile.T == 5 or Tile.T == 6 or Tile.T == 7:
                    if Brake == False:
                        Brake = True
                        BrakeT = 50
                        Bi = Tile.i
                        Bq = Tile.q
            if Tile.R.colliderect(mouseRect) and Tile.R.colliderect(PlayerI) and Tile.T == 26 and event.type == MOUSEBUTTONDOWN and event.button == 1:
                for Slot in Slots:
                    if Slot.T == 2: 
                        if Brake == False:
                            Brake = True
                            BrakeT = 50
                            Bi = Tile.i
                            Bq = Tile.q
            if Tile.R.colliderect(mouseRect) and Tile.R.colliderect(PlayerI) and Tile.T == 29 and event.type == MOUSEBUTTONDOWN and event.button == 1:
                Open = False
                for Slot in Slots:
                    if Slot.T == 2 and Open == False:
                        Slot.T = 0
                        Slot.A -= 1
                        Open = True
                        
                if Open == True:
                    tiles[Tile.i][Tile.q] = 0
                    Tile.T = tiles[Tile.i][Tile.q]
        
        else:
            if Tile.R.colliderect(mouseRect) and Tile.R.colliderect(PlayerI) and Tile.i == 3 and Tile.q == 16 and Tile.T == 4 and MOSI == True:
                tiles[18][27] = 0
                tiles[Tile.i][Tile.q] = 12
                Tile.T = tiles[Tile.i][Tile.q]
            if Tile.R.colliderect(mouseRect) and Tile.R.colliderect(PlayerI) and Tile.T == 18 and MOSI == True:
                tiles[Tile.i][Tile.q] = 17
                Tile.T = tiles[Tile.i][Tile.q]
                x = Tile.x - X - X + 5 + random.randint(-5, 5)
                y = Tile.y - Y - Y + 5 + random.randint(-5, 5)
                ItemT = 3
                Items.append(ITEM(X,Y,x,y,ItemT))
                        
            if Tile.R.colliderect(mouseRect) and Tile.R.colliderect(PlayerI) and Tile.T == 2 and MOSI == True:
                if Brake == False:
                    Brake = True
                    BrakeT = 50
                    Bi = Tile.i
                    Bq = Tile.q
            if Tile.R.colliderect(mouseRect) and Tile.R.colliderect(PlayerI) and MOSI == True:
                if Tile.T == 5 or Tile.T == 6 or Tile.T == 7:
                    if Brake == False:
                        Brake = True
                        BrakeT = 50
                        Bi = Tile.i
                        Bq = Tile.q
            if Tile.R.colliderect(mouseRect) and Tile.R.colliderect(PlayerI) and Tile.T == 26 and MOSI == True:
                for Slot in Slots:
                    if Slot.T == 2: 
                        if Brake == False:
                            Brake = True
                            BrakeT = 50
                            Bi = Tile.i
                            Bq = Tile.q
            if Tile.R.colliderect(mouseRect) and Tile.R.colliderect(PlayerI) and Tile.T == 29 and MOSI == True:
                Open = False
                for Slot in Slots:
                    if Slot.T == 2 and Open == False:
                        Slot.T = 0
                        Slot.A -= 1
                        Open = True
                        
                if Open == True:
                    tiles[Tile.i][Tile.q] = 0
                    Tile.T = tiles[Tile.i][Tile.q]

                    


                
        
            
        if Tile.T == 1:
            Tile.I = Wall
        elif Tile.T == 0:
            Tile.I = Floor
        elif Tile.T == 2:
            Tile.I = LChest
        elif Tile.T == 3:
            Tile.I = Fountain
        elif Tile.T == 4:
            Tile.I = CLever
        elif Tile.T == 5:
            Tile.I = Crate1
        elif Tile.T == 6:
            Tile.I = Crate2
        elif Tile.T == 7:
            Tile.I = Crate3
        elif Tile.T == 8:
            Tile.I = Plant
        elif Tile.T == 9:
            Tile.I = Bed
        elif Tile.T == 10:
            Tile.I = WR
        elif Tile.T == 11:
            Tile.I = AR
        elif Tile.T == 12:
            Tile.I = OLever
        elif Tile.T == 13:
            Tile.I = Anvil
        elif Tile.T == 14:
            Tile.I = Oven
        elif Tile.T == 15:
            Tile.I = GrindStone
        elif Tile.T == 16:
            Tile.I = SmithTable
        elif Tile.T == 17:
            Tile.I = OrbT
        elif Tile.T == 18:
            Tile.I = Orb
        elif Tile.T == 19:
            Tile.I = NTrap
        elif Tile.T == 20:
            Tile.I = ETrap
        elif Tile.T == 21:
            Tile.I = OChest
        elif Tile.T == 22:
            Tile.I = Table
        elif Tile.T == 23:
            Tile.I = Counter
        elif Tile.T == 24:
            Tile.I = Spit
        elif Tile.T == 25:
            Tile.I = Book
        elif Tile.T == 26:
            Tile.I = LGChest
        elif Tile.T == 27:
            Tile.I = OGChest
        elif Tile.T == 28:
            Tile.I = TRack
        elif Tile.T == 29:
            Tile.I = Lock
        elif Tile.T == 30:
            Tile.I = Plant2
        elif Tile.T == 31:
            Tile.I = Crack
        elif Tile.T == 32:
            Tile.I = Desk
        elif Tile.T == 33:
            Tile.I = Shelf
              
        Tile.SI = pygame.transform.scale(Tile.I, (50, 50))
        
        if Tile.R.colliderect(player) and Tile.T == 20:
            if HCD < 0:
                Lives -= 1
                HCD = 20
    
    
    if Xbox == False:        
        BrakeR = pygame.Rect(mousex, mousey + 30, BrakeT / 2, 3)
    else:
        BrakeR = pygame.Rect(mX, mY + 30, BrakeT / 2, 3)
    
    
        
    
        
    for Tile in Tiles:
        Tile.x = Tile.X + X
        Tile.y = Tile.Y + Y
        Tile.R = pygame.Rect(Tile.x, Tile.y, 50, 50)
        Tile.SI = pygame.transform.scale(Tile.I, (50, 50))
        if Tile.R.colliderect(MIDDLE):
            Tile.draw(windowSurface)
    
    
    for Item in Items:
        Item.x = Item.X + X
        Item.y = Item.Y + Y
        #print(Item.x)
        pickup = False
        Unstack = False
        Item.R = pygame.Rect(Item.x, Item.y, 20, 20)
        if Xbox == False:
            if Item.R.colliderect(mouseRect)and Item.R.colliderect(PlayerI) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                for Slot in Slots:
                    if Slot.E == True and Item.T not in inventory:
                        Slot.E = False
                        Slot.T = Item.T
                        Slot.A += 1
                        Slot.TL = Item.TL
                        inventory.append(Item.T)
                        pickup = True
                    if Slot.T == Item.T and Item.T in Stackable and pickup == False:
                        Slot.A += 1
                        Slot.TL = Item.TL
                        pickup = True
                    if Item.T not in Stackable and Slot.E == True and Unstack == False and pickup == False:
                        Slot.E = False
                        Slot.T = Item.T
                        Slot.A += 1
                        Slot.TL = Item.TL
                        inventory.append(Item.T)
                        #print(inventory)
                        pickup = True
                        Unstack = True
                        
                        
            if pickup == True:
                Items.pop(Items.index(Item))
        else:
            if Item.R.colliderect(mouseRect)and Item.R.colliderect(PlayerI) and MOSI == True:
                for Slot in Slots:
                    if Slot.E == True and Item.T not in inventory:
                        Slot.E = False
                        Slot.T = Item.T
                        Slot.A += 1
                        inventory.append(Item.T)
                        pickup = True
                    if Slot.T == Item.T and Item.T in Stackable and pickup == False:
                        Slot.A += 1
                        pickup = True
                    if Item.T not in Stackable and Slot.E == True and Unstack == False and pickup == False:
                        Slot.E = False
                        Slot.T = Item.T
                        Slot.A += 1
                        inventory.append(Item.T)
                        #print(inventory)
                        pickup = True
                        Unstack = True
                        
                        
            if pickup == True:
                Items.pop(Items.index(Item))
                    
                    
        
                    
        if Item.R.colliderect(MIDDLE):
            Item.draw(windowSurface)
            
    for BadGuy in BadGuys:
        BadGuy.draw(windowSurface)
            
    pygame.draw.rect(windowSurface, BLACK, TOP)
    pygame.draw.rect(windowSurface, BLACK, BOTTOM)
    pygame.draw.rect(windowSurface, BLACK, RIGHT)
    pygame.draw.rect(windowSurface, BLACK, LEFT)
    windowSurface.blit(MIDDLESI,MIDDLE)
    pygame.draw.rect(windowSurface, (50, 50, 50), HR)
    
    #pygame.draw.rect(windowSurface, (255,0,0), player)
    
    
    if Brake == True:
        pygame.draw.rect(windowSurface, BLACK, BrakeR)
        BrakeT -= 1
        for Tile in Tiles:
            if Bi == Tile.i and Bq == Tile.q:
                if mouseRect.colliderect(Tile.R):
                    if BrakeT < 0:
                        if Tile.T == 5 or Tile.T == 6 or Tile.T == 7:
                            random.shuffle(CrateLT)
                            x = Tile.x - X - X + random.randint(10, 30)
                            y = Tile.y - Y - Y + random.randint(10, 30)
                            ItemT = CrateLT[0]
                            if ItemT == 6:
                                TL = TreasureL[random.randint(0,len(TreasureL)-1)]
                            else:
                                TL = [0,0]
                            if ItemT != 0:
                                Items.append(ITEM(x,y,X,Y,ItemT,TL))
                            x = Tile.x - X - X + random.randint(10, 30)
                            y = Tile.y - Y - Y + random.randint(10, 30)
                            ItemT = CrateLT[1]
                            if ItemT == 6:
                                TL = TreasureL[random.randint(0,len(TreasureL)-1)]
                            else:
                                TL = [0,0]
                            if ItemT != 0:
                                Items.append(ITEM(x,y,X,Y,ItemT,TL))
                            tiles[Tile.i][Tile.q] = 0
                            Tile.T = tiles[Tile.i][Tile.q]
                            Brake = False
                            BrakeT = 0
                        if Tile.T == 2:
                            random.shuffle(ChestLT)
                            x = Tile.x - X - X + random.randint(10, 30)
                            y = Tile.y - Y - Y + random.randint(10, 30)
                            ItemT = ChestLT[0]
                            if ItemT == 6:
                                TL = TreasureL[random.randint(0,len(TreasureL)-1)]
                            else:
                                TL = [0,0]
                            if ItemT != 0:
                                Items.append(ITEM(x,y,X,Y,ItemT,TL))
                            x = Tile.x - X - X + random.randint(10, 30)
                            y = Tile.y - Y - Y + random.randint(10, 30)
                            ItemT = ChestLT[1]
                            if ItemT == 6:
                                TL = TreasureL[random.randint(0,len(TreasureL)-1)]
                            else:
                                TL = [0,0]
                            if ItemT != 0:
                                Items.append(ITEM(x,y,X,Y,ItemT,TL))
                            x = Tile.x - X - X + random.randint(10, 30)
                            y = Tile.y - Y - Y + random.randint(10, 30)
                            ItemT = ChestLT[2]
                            if ItemT == 6:
                                TL = TreasureL[random.randint(0,len(TreasureL)-1)]
                            else:
                                TL = [0,0]
                            if ItemT != 0:
                                Items.append(ITEM(x,y,X,Y,ItemT,TL))
                            tiles[Tile.i][Tile.q] = 21
                            Tile.T = tiles[Tile.i][Tile.q]
                            Brake = False
                            BrakeT = 0
                        if Tile.T == 26:
                            random.shuffle(GChestLT)
                            x = Tile.x - X - X + random.randint(10, 30)
                            y = Tile.y - Y - Y + random.randint(10, 30)
                            ItemT = GChestLT[0]
                            if ItemT == 6:
                                TL = TreasureL[random.randint(0,len(TreasureL)-1)]
                            else:
                                TL = [0,0]
                            if ItemT != 0:
                                Items.append(ITEM(x,y,X,Y,ItemT,TL))
                            x = Tile.x - X - X + random.randint(10, 30)
                            y = Tile.y - Y - Y + random.randint(10, 30)
                            ItemT = GChestLT[1]
                            if ItemT == 6:
                                TL = TreasureL[random.randint(0,len(TreasureL)-1)]
                            else:
                                TL = [0,0]
                            if ItemT != 0:
                                Items.append(ITEM(x,y,X,Y,ItemT,TL))
                            x = Tile.x - X - X + random.randint(10, 30)
                            y = Tile.y - Y - Y + random.randint(10, 30)
                            ItemT = GChestLT[2]
                            if ItemT == 6:
                                TL = TreasureL[random.randint(0,len(TreasureL)-1)]
                            else:
                                TL = [0,0]
                            if ItemT != 0:
                                Items.append(ITEM(x,y,X,Y,ItemT,TL))
                            ItemT = GChestLT[3]
                            if ItemT == 6:
                                TL = TreasureL[random.randint(0,len(TreasureL)-1)]
                            else:
                                TL = [0,0]
                            if ItemT != 0:
                                Items.append(ITEM(x,y,X,Y,ItemT,TL))
                            x = Tile.x - X - X + random.randint(10, 30)
                            y = Tile.y - Y - Y + random.randint(10, 30)
                            ItemT = GChestLT[4]
                            if ItemT == 6:
                                TL = TreasureL[random.randint(0,len(TreasureL)-1)]
                            else:
                                TL = [0,0]
                            if ItemT != 0:
                                Items.append(ITEM(x,y,X,Y,ItemT,TL))
                            tiles[Tile.i][Tile.q] = 27
                            Tile.T = tiles[Tile.i][Tile.q]
                            Brake = False
                            BrakeT = 0
                            tiles[Tile.i][Tile.q] = 27
                            Tile.T = tiles[Tile.i][Tile.q]
                            Brake = False
                            BrakeT = 0
                            DEL = False
                            for Slot in Slots:
                                if Slot.T == 2 and DEL == False:
                                    DEL = True
                                    Slot.A -= 1
                                

                else:
                    Brake = False
                    BrakeT = 0
    

    for Slot in Slots:
        if Xbox == False:
            if Slot.R.colliderect(mouseRect) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                Slot.SS = True
                for Slot in Slots:
                    Slot.S = False
            if Slot.SS == True:
                Slot.S = True
                Slot.SS = False
            
                
                
                    
    for Slot in Slots:
        Stop = False
        if Slot.S == True:
            treasure = Slot.TL
            if Slot.T == 6:
                TT = True
            else:
                TT = False
        if Slot.S == True and Slot.T in Weapons and event.type == MOUSEBUTTONDOWN and event.button == 1:
            Attack = True
            AttackT = Slot.T
        
        if Xbox == False:
            if Slot.S == True and event.type == KEYDOWN and event.key == K_q and Slot.A > 0:
                Slot.A -= 1
                x = player.x - X - X + 5 + random.randint(-5, 5)
                y = player.y - Y - Y + 5 + random.randint(-5, 5)
                ItemT = Slot.T
                Items.append(ITEM(X,Y,x,y,ItemT,TL))
            if Slot.S == True and Slot.T == 4 and USECD < 0 and not mouseRect.colliderect(HR):
                if event.type == MOUSEBUTTONDOWN and event.button == 3:
                    a = random.randint(0,len(TP)-1)
                    X = TP[a][0]
                    Y = TP[a][1]
                    LX = X
                    LY = Y
                    Slot.A -= 1
                    USECD = 50
        else:
            if Slot.S == True and event.type == KEYDOWN and MOSQ == True and Slot.A > 0:
                Slot.A -= 1
                x = player.x - X - X + 5 + random.randint(-5, 5)
                y = player.y - Y - Y + 5 + random.randint(-5, 5)
                ItemT = Slot.T
                Items.append(ITEM(X,Y,x,y,ItemT))
            if Slot.S == True and Slot.T == 4 and USECD < 0 and event.type == MOUSEBUTTONDOWN and not mouseRect.colliderect(HR):
                a = random.randint(0,len(TP)-1)
                X = TP[a][0]
                Y = TP[a][1]
                LX = X
                LY = Y
                Slot.A -= 1
                USECD = 50

                    
        if Slot.A == 0:
            Slot.E = True
            if Slot.T in inventory and Slot.T in Stackable:
                Slot.E = True
                inventory.remove(Slot.T)
                Slot.T = 0
            if Slot.T in inventory and Slot.T not in Stackable:
                for i in range(0, len(inventory)-1):
                    if inventory[i] == Slot.T and Stop == False:
                        inventory.pop(i)
                        Stop = True
            Slot.T = 0
    #print(len(BadGuys))
    #pygame.draw.rect(windowSurface,(255,0,0),player)
    TEX = basicFont.render(str(X), True, (50,50,50))
    TRX = Slot.TE.get_rect()
    TRX.centerx = (900)
    TRX.centery = (40)
    TEY = basicFont.render(str(Y), True, (50,50,50))
    TRY = Slot.TE.get_rect()
    TRY.centerx = (850)
    TRY.centery = (40)
    windowSurface.blit(TEX, TRX)
    windowSurface.blit(TEY, TRY)
    
    if Attack == True:
        if AttackCD < -20:
            if AttackT == 8 or AttackT == 7:
                AttackCD = 8
            elif AttackT == 9:
                AttackCD = 25
        if AttackCD > 0:
            if playerI in WalkD:
                if AttackT == 7:
                    WeaponR = pygame.Rect(player.centerx - 5,player.bottom + 6 - AttackCD,10,24)
                    WeaponI = pygame.image.load('IronSwordDown.png')
                elif AttackT == 8:
                    WeaponR = pygame.Rect(player.centerx - 5,player.bottom + 6 - AttackCD,10,24)
                    WeaponI = pygame.image.load('BoneSwordDown.png')
                elif AttackT == 9:
                    WeaponR = pygame.Rect(player.centerx - 5,player.bottom + 15 - AttackCD,10,36)
                    WeaponI = pygame.image.load('SpearDown.png')
            if playerI in WalkU:
                if AttackT == 7:
                    WeaponR = pygame.Rect(player.centerx - 5,player.top - 30 + AttackCD,10,24)
                    WeaponI = pygame.image.load('IronSwordUp.png')
                elif AttackT == 8:
                    WeaponR = pygame.Rect(player.centerx - 5,player.top - 30 + AttackCD,10,24)
                    WeaponI = pygame.image.load('BoneSwordUp.png')
                elif AttackT == 9:
                    WeaponR = pygame.Rect(player.centerx - 5,player.top - 44 + AttackCD,10,36)
                    WeaponI = pygame.image.load('SpearUp.png')
            if playerI in WalkL:
                if AttackT == 7:
                    WeaponR = pygame.Rect(player.left - 28 + AttackCD, player.centery - 5,24,10)
                    WeaponI = pygame.image.load('IronSwordLeft.png')
                elif AttackT == 8:
                    WeaponR = pygame.Rect(player.left - 28 + AttackCD, player.centery - 5,24,10)
                    WeaponI = pygame.image.load('BoneSwordLeft.png')
                elif AttackT == 9:
                    WeaponR = pygame.Rect(player.left - 40 + AttackCD, player.centery - 5,36,10)
                    WeaponI = pygame.image.load('SpearLeft.png')
            if playerI in WalkR:
                if AttackT == 7:
                    WeaponR = pygame.Rect(player.right + 2 - AttackCD, player.centery - 5,24,10)
                    WeaponI = pygame.image.load('IronSwordRight.png')
                elif AttackT == 8:
                    WeaponR = pygame.Rect(player.right + 2 - AttackCD, player.centery - 5,24,10)
                    WeaponI = pygame.image.load('BoneSwordRight.png')
                elif AttackT == 9:
                    WeaponR = pygame.Rect(player.right + 8 - AttackCD, player.centery - 5,36,10)
                    WeaponI = pygame.image.load('SpearRight.png')            
            #pygame.draw.rect(windowSurface,BLACK,WeaponR)
            windowSurface.blit(WeaponI,WeaponR)
        if AttackCD < 0:
            Attack = False
            
    AttackCD -= 1

    windowSurface.blit(playerSI, (player.x, player.y - 5))
    
    if treasure[1] > X and TT == True:
        windowSurface.blit(LASI,(465,272))
    elif treasure[1] < X and TT == True:
        windowSurface.blit(RASI,(480,272))
    if treasure[0] > Y and TT == True:
        windowSurface.blit(UASI,(475,265))
    elif treasure[0] < Y and TT == True:
        windowSurface.blit(DASI,(475,280))
        
        
        
        
    #print(len(Items))
    
    HCD -= 1
    
    if Lives == -1:
        time.sleep(3)
        pygame.quit()
        sys.exit
    
   
    
    for Heart in hearts:
        if Lives < Heart.N:
            Heart.I = HeartI[1]
        else:
            Heart.I = HeartI[0]
        Heart.SI = pygame.transform.scale(Heart.I, (40, 40))
        Heart.draw(windowSurface)
    for Slot in Slots:
        Slot.TE = basicFont.render(str(Slot.A), True, (50,50,50))
        Slot.TR = Slot.TE.get_rect()
        Slot.TR.centerx = (Slot.x + 40)
        Slot.TR.centery = (Slot.y + 40)
        Slot.I = SlotI[Slot.T]
        if Slot.S == False:
            Slot.SI = pygame.transform.scale(Slot.I, (50, 50))
        else:
            Slot.SI = pygame.transform.scale(Slot.I, (60, 60))
        Slot.draw(windowSurface)
        
    windowSurface.blit(MouseSI, mouseRect)
    
    USECD -= 1
    
    pygame.display.update()
    mainClock.tick(40)
        
