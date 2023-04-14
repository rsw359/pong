import pygame
from colors import *
import math
import random


class Ball:
    MAX_VEL = 5  # maximum velocity of the ball
    RADIUS = 7  # radius of the ball
    COLOR = GREEN

    def __init__(self, x, y, radius, color):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius

        angle = self.get_random_angle(-30, 30, [0])
        position = 1 if random.random() < 0.5 else -1

        # x velocty = absolute value of the cosine of the angle times the maximum velocity of the ball. This is done to ensure that the ball does not move backwards
        self.x_vel = position * abs(math.cos(angle) * self.MAX_VEL)
        # y velocity = sine of the angle times the maximum velocity of the ball. determines the vertical speed of the ball
        self.y_vel = math.sin(angle) * self.MAX_VEL

    def get_random_angle(self, min, max, exclude):
        angle = 0
        while angle in exclude:
            angle = math.radians(random.randint(min, max))

        return angle

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.RADIUS)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

        angle = self.get_random_angle(-30, 30, [0])

        # When the reset method is called, it means that the ball has gone out of bounds and needs to be repositioned and given a new direction and speed.
        self.x_vel = abs(math.cos(angle) * self.MAX_VEL)
        self.y_vel = math.sin(angle) * self.MAX_VEL

        # The ball will always move towards the player who lost the point. This is done by multiplying the x velocity by -1. This will cause the ball to move in the opposite direction. The y velocity is set to 0 because the ball should not move vertically when it is reset.
        self.y_vel = 0  # the ball should not move vertically when it is reset
        self.x_vel *= -1  # reverses the x direction of the ball
