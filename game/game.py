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
            tiles[x].append(Tile(x * TILE_LENGTH, y * TILE_LENGTH, FLOOR))
    tiles[0][0].change_type(START)
    tiles[FIELD_SIZE - 1][FIELD_SIZE - 1].change_type(END)
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
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                for button in buttons:
                    if (button.position.x <= mouse_x <= button.position.x2) and (
                            button.position.y <= mouse_y <= button.position.y2):
                        print('button is selected')
                for row in map_tiles:
                    for tile in row:
                        if (tile.position.x <= mouse_x <= tile.position.x2) and (
                                tile.position.y <= mouse_y <= tile.position.y2):
                            if tile.typeTyle == FLOOR:
                                tile.change_type(WALL)
                                tile.draw(DISPLAY_SURFACE)
                            else:
                                tile.change_type(FLOOR)
                                tile.draw(DISPLAY_SURFACE)

    pygame.display.update()

