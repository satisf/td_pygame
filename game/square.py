from config import *

class Square:
    def __init__(self, x, y, width, height):
        self.x = x
        self.x2 = x + width
        self.y = y
        self.y2 = y + height
        self.width = width
        self.height = height
