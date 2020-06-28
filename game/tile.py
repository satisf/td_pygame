import pygame
from position import Position
from config import *

class Tile:
    def __init__(self, x, y, colour, tiletype):
        self.position = Position(x, y)
        self.colour = colour
        self.typeTyle = tiletype

    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, (self.position.x * TILE_LENGTH, self.position.y * TILE_LENGTH, TILE_LENGTH, TILE_LENGTH), BORDER_SIZE)
