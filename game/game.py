import sys
import pygame
from pygame.locals import *
from config import *
from tile import Tile
from button import Button

pygame.init()


def generate_map_tiles():
    tiles = []
    for x in range(FIELD_SIZE):
        tiles.append([])
        for y in range(FIELD_SIZE):
            tiles[x].append(Tile(x * TILE_LENGTH, y * TILE_LENGTH, BLACK, FLOOR))
    return tiles

def generate_buttons():
    buttons = []
    buttons.append(Button((FIELD_SIZE + 1) * TILE_LENGTH, 0 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, 'TOGGLE'))
    return buttons


DISPLAY_SURFACE = pygame.display.set_mode((SURFACE_WIDTH, SURFACE_HEIGHT))


map_tiles = generate_map_tiles()
buttons = generate_buttons()


def draw_map(surface, tiles):
    surface.fill(WHITE)
    for x in range(len(tiles)):
        for y in range(len(tiles[x])):
            tiles[x][y].draw(surface)


def draw_buttons(surface, btns):
    for button in btns:
        button.draw(surface)


pygame.display.set_caption('PyGame Tower Defence')
draw_map(DISPLAY_SURFACE, map_tiles)
draw_buttons(DISPLAY_SURFACE, buttons)



# main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

