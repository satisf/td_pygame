import math
import pygame
from config import *

class Tower:
    def __init__(self, tile):
        self.tile = tile

    def reposition(self, tile):
        self.tile = tile

    def shoot(self, enemies, surface):
        for enemy in enemies:
            if is_in_range(self.tile.middle, enemy):
                enemy.hit()
                self.draw_shot(enemy, surface)
                return
        return

    def draw_shot(self, enemy, surface):
        pygame.draw.line(surface, RED, (self.tile.middle.x, self.tile.middle.y), (enemy.position.x, enemy.position.y), 1)


def is_in_range(position, enemy):
    distance = math.sqrt(pow((enemy.position.x - position.x), 2) + pow((enemy.position.y - position.y), 2))
    if distance <= TOWER_RANGE:
        return True
    return False
