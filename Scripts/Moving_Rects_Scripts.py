import pygame


class Moving_Rect:
    def __init__(self, rect):
        self.rect = rect
    

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    