import pygame
from square import Square
from config import *


class Button:
    def __init__(self, x, y, width, height, text):
        self.position = Square(x, y, width, height)
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface,
                         BLACK,
                         (self.position.x, self.position.y, self.position.width, self.position.height),
                         BORDER_SIZE)
