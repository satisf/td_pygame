import pygame
from position import Position
from config import *

class Tile:
    def __init__(self, x, y, tiletype):
        self.position = Position(x, y, TILE_LENGTH, TILE_LENGTH)
        self.typeTyle = FLOOR
        self.change_type(tiletype)


    def change_type(self, type):
        if self.typeTyle == START or self.typeTyle == END:
            return
        if type == WALL:
            self.typeTyle = WALL
            self.colour = BLACK
            self.border = 0
        elif type == FLOOR:
            self.typeTyle = FLOOR
            self.colour = BLACK
            self.border = BORDER_SIZE
        elif type == START:
            self.typeTyle = START
            self.colour = GREEN
            self.border = 0
        elif type == END:
            self.typeTyle = END
            self.colour = RED
            self.border = 0



    def draw(self, surface):
        pygame.draw.rect(surface,
                         WHITE,
                         (self.position.x, self.position.y, self.position.width, self.position.height),
                         0)
        pygame.draw.rect(surface,
                         self.colour,
                         (self.position.x, self.position.y, self.position.width, self.position.height),
                         self.border)

