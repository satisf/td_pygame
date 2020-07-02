import pygame
from config import *

class Enemy:
    def __init__(self, position, colour):
        self.position = position
        self.colour = colour

    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.position.x, self.position.y), ENEMY_SIZE)

    def move(self, direction):
        if direction == LEFT:
            self.position.x -= TILE_LENGTH
        elif direction == RIGHT:
            self.position.x += TILE_LENGTH
        elif direction == UP:
            self.position.y -= TILE_LENGTH
        elif direction == DOWN:
            self.position.y += TILE_LENGTH

