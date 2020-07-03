import pygame
from config import *

class Enemy:
    def __init__(self, position, colour):
        self.position = position
        self.colour = colour
        self.health = INITIAL_ENEMY_HEALTH

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

    def hit(self):
        self.health -=1

    def has_reached_end(self, end):
        if (end.square.x < self.position.x < end.square.x2) and (
                end.square.y < self.position.y < end.square.y2):
            return True
        return False
