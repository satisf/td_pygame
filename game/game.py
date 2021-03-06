import sys
import pygame
import time
import pygame.freetype
from pygame.locals import *
from config import *
from tile import Tile
from tower import Tower
from button import Button
from enemy import Enemy
from position import Position
from pathfinding import find_path


def generate_map_tiles():
    tiles = []
    for x in range(FIELD_SIZE):
        tiles.append([])
        for y in range(FIELD_SIZE):
            tiles[x].append(Tile(Position(x, y), x * TILE_LENGTH, y * TILE_LENGTH, FLOOR))
    tiles[0][0].change_type(START)
    tiles[FIELD_SIZE - 1][FIELD_SIZE - 1].change_type(END)
    return tiles

def add_enemy(enemies):
    enemies.append(Enemy(Position(int(TILE_LENGTH / 2), int(TILE_LENGTH / 2)), RED))



def generate_buttons():
    buttons = []
    buttons.append(Button((FIELD_SIZE + 1) * TILE_LENGTH, 3 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, 'TOGGLE'))
    return buttons


def draw_map(surface, tiles):
    surface.fill(WHITE)
    for x in range(len(tiles)):
        for y in range(len(tiles[x])):
            tiles[x][y].draw(surface)


def draw_buttons(surface, btns):
    for button in btns:
        button.draw(surface)


def draw_enemies(surface, enemies):
    for enemy in enemies:
        enemy.draw(surface)


def draw_text(surface, game_state, font):
    if game_state is BUILD_TOWER:
        font.render_to(surface, ((FIELD_SIZE + 1) * TILE_LENGTH, 0), 'place a tower and continue', BLACK)
        font.render_to(surface, ((FIELD_SIZE + 1.2) * TILE_LENGTH, 3.2 * TILE_LENGTH), 'continue', BLACK)
    elif game_state is BUILD_WALLS:
        font.render_to(surface, ((FIELD_SIZE + 1) * TILE_LENGTH, 0), 'place some walls and start', BLACK)
        font.render_to(surface, ((FIELD_SIZE + 1.2) * TILE_LENGTH, 3.2 * TILE_LENGTH), 'start', BLACK)
    elif game_state is WIN:
        font.render_to(surface, ((FIELD_SIZE + 1) * TILE_LENGTH, 0), 'You win \o/', BLACK)
    elif game_state is LOST:
        font.render_to(surface, ((FIELD_SIZE + 1) * TILE_LENGTH, 0), 'You lost :( ', BLACK)


def find_direction(enemy, path):
    for i in range(len(path) - 1):
        if (path[i].square.x < enemy.position.x < path[i].square.x2) and (
                path[i].square.y < enemy.position.y < path[i].square.y2):
            if path[i].position.x < path[i+1].position.x:
                return RIGHT
            elif path[i].position.x > path[i+1].position.x:
                return LEFT
            elif path[i].position.y > path[i+1].position.y:
                return UP
            elif path[i].position.y < path[i+1].position.y:
                return DOWN


def draw_everything():
    draw_map(DISPLAY_SURFACE, map_tiles)
    if game_state is BUILD_TOWER or game_state is BUILD_WALLS:
        draw_buttons(DISPLAY_SURFACE, buttons)
    draw_enemies(DISPLAY_SURFACE, enemies)
    draw_text(DISPLAY_SURFACE, game_state, FONT)


pygame.init()
pygame.display.set_caption('PyGame Tower Defence')


DISPLAY_SURFACE = pygame.display.set_mode((SURFACE_WIDTH, SURFACE_HEIGHT))
FONT = pygame.freetype.SysFont(None, 12)
map_tiles = generate_map_tiles()
start = map_tiles[0][0]
end = map_tiles[FIELD_SIZE - 1][FIELD_SIZE - 1]
tower = Tower(start)
buttons = generate_buttons()
enemies = []
add_enemy(enemies)
game_state = BUILD_TOWER

draw_everything()


# main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif (event.type == MOUSEBUTTONDOWN) and game_state is not RUNNING:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                for button in buttons:
                    if (button.square.x <= mouse_x <= button.square.x2) and (
                            button.square.y <= mouse_y <= button.square.y2):
                        path = find_path(map_tiles, map_tiles[0][0])
                        if game_state is BUILD_TOWER:
                            game_state = BUILD_WALLS
                        elif game_state is BUILD_WALLS:
                            game_state = RUNNING
                for row in map_tiles:
                    for tile in row:
                        if (tile.square.x <= mouse_x <= tile.square.x2) and (
                                tile.square.y <= mouse_y <= tile.square.y2):
                            if game_state is BUILD_WALLS:
                                if tile.typeTyle == FLOOR:
                                    tile.change_type(WALL)
                                else:
                                    tile.change_type(FLOOR)
                            elif game_state is BUILD_TOWER:
                                if tower:
                                    tower.tile.set_type(FLOOR)
                                tower.tile = tile
                                tile.change_type(TOWER)
    if game_state is RUNNING:
        tower.shoot(enemies, DISPLAY_SURFACE)
        pygame.display.update()
        if len(enemies) == 0:
            game_state = WIN
        for enemy in enemies:
            if enemy.health == 0:
                enemies.remove(enemy)
                continue
            enemy.move(find_direction(enemy, path))
            if enemy.has_reached_end(end):
                game_state = LOST
        time.sleep(0.5)

    draw_everything()
    pygame.display.update()

