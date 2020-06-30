import pygame
from position import Position
from config import *

class Tile:
    def __init__(self, x, y, tiletype):
        self.position = Position(x, y, TILE_LENGTH, TILE_LENGTH)
        self.change_type(tiletype)


    def change_type(self, type):
        if type == WALL:
            self.typeTyle = WALL
            self.colour = BLACK
            self.border = 0
        elif type == FLOOR:
            self.typeTyle = FLOOR
            self.colour = BLACK
            self.border = BORDER_SIZE


    def draw(self, surface):
        pygame.draw.rect(surface,
                         WHITE,
                         (self.position.x, self.position.y, self.position.width, self.position.height),
                         0)
        pygame.draw.rect(surface,
                         self.colour,
                         (self.position.x, self.position.y, self.position.width, self.position.height),
                         self.border)

