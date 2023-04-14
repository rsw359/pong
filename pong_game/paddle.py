import pygame
from colors import *


class Paddle:
    COLOR = WHITE
    VEL = 4
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, x, y, width, height):  # initializes the paddle
        self.x = self.original_x = x
        self.y = self.original_y = y

    def draw(self, win):  # draws the paddle
        pygame.draw.rect(
            win, self.COLOR, (self.x, self.y, self.WIDTH, self.HEIGHT))

    def move(self, up=True):
        if up:
            self.y -= self.VEL  # upward movement subtracts from the velocity, moves the paddle up
        else:
            self.y += self.VEL  # downward movement adds to the velocity, moves the paddle down

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
