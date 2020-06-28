import sys
import pygame
from pygame.locals import *

pygame.init()



# set up the colors

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

TILE_LENGTH = 30
FIELD_SIZE = 10
BORDER_SIZE = 1



def draw_map(surface, fieldSize, tileLength, border, color):
    surface.fill(WHITE)
    for x in range(fieldSize):
        for y in range(fieldSize):
            pygame.draw.rect(surface, color, (x * tileLength, y * tileLength, tileLength, tileLength), border)

DISPLAYSURF = pygame.display.set_mode((500, 300))

draw_map(DISPLAYSURF, FIELD_SIZE, TILE_LENGTH, BORDER_SIZE, BLACK)

pygame.display.set_caption('PyGame Tower Defence')


# main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

