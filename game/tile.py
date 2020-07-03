import pygame
from square import Square
from position import Position
from config import *

class Tile:
    def __init__(self, position, x, y, tiletype):
        self.position = position
        self.square = Square(x, y, TILE_LENGTH, TILE_LENGTH)
        self.middle = Position(x + (TILE_LENGTH / 2), y + (TILE_LENGTH / 2))
        self.typeTyle = FLOOR
        self.colour = WHITE
        self.border = BORDER_SIZE
        self.neighbours = []
        self.estimated_distance_to_end = FIELD_SIZE * FIELD_SIZE
        self.change_type(tiletype)

    def change_type(self, type):
        if self.typeTyle == START or self.typeTyle == END or self.typeTyle == TOWER:
            return
        self.set_type(type)

    def set_type(self, type):
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
        elif type == TOWER:
            self.typeTyle = TOWER
            self.colour = BLUE
            self.border = 0
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
                         self.colour,
                         (self.square.x, self.square.y, self.square.width, self.square.height),
                         self.border)

