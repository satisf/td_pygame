import pygame
from square import Square
from config import *


class Button:
    def __init__(self, x, y, width, height, text):
        self.square = Square(x, y, width, height)
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface,
                         BLACK,
                         (self.square.x, self.square.y, self.square.width, self.square.height),
                         BORDER_SIZE)
