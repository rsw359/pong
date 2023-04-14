import pygame
from .colors import *
from .paddle import Paddle
from .ball import Ball
import random
pygame.init()  # initializes pygame


FPS = 60  # sets the fps of the game
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # sets the size of the window
BALL_RADIUS = 7
# sets the font of the score
SCORE_FONT = pygame.font.Font("fonts/neon-80s/Neon.ttf", 30)
WIN_SCORE_FONT = pygame.font.Font("fonts/neon-80s/Neon.ttf", 50)

pygame.display.set_caption("Pong!")  # sets the title of the window


WINNING_SCORE = 2  # sets the winning score to 10


class GameInfo:
    def __init__(self, left_hit_count, right_hit_count, left_score, right_score):
        self.left_hit_count = left_hit_count
        self.right_hit_count = right_hit_count
        self.left_score = left_score
        self.right_score = right_score


class Pong:
    SCORE_FONT = pygame.font.Font("fonts/neon-80s/Neon.ttf", 30)

    def __init__(self, window, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        self.left_paddle = Paddle(10, window_height//2 - Paddle.HEIGHT//2)
        self.right_paddle = Paddle(
            window_width - 10 - Paddle.WIDTH, window_height//2 - Paddle.HEIGHT//2)
        self.ball = Ball(window_width//2, window_height//2)

        self.left_score = 0
        self.right_score = 0
        self.left_hit_count = 0
        self.right_hit_count = 0
        self.window = window

    def _draw_score(self):
        left_score_text = self.SCORE_FONT.render(
            f"{self.left_score}", 1, self.WHITE)
        right_score_text = self.SCORE_FONT.render(
            f"{self.right_score}", 1, self.WHITE)
        self.window.blit(left_score_text, (self.window_width //
                                           4 - left_score_text.get_width()//2, 20))
        self.window.blit(right_score_text, (self.window_width * (3/4) -
                                            right_score_text.get_width()//2, 20))

    def _draw_hit_count(self):
        hit_count_text = self.SCORE_FONT.render(
            f"{self.left_hit_count + self.right_hit_count}", 1, self.RED)
        self.window.blit(hit_count_text, (self.window_width //
                                          2 - hit_count_text.get_width()//2, 10))

    def draw_divider(self):

        circle_radius = HEIGHT // 200

        for i in range(10, self.window_height, self.window_height//20):
            if i % 2 == 1:
                continue
            pygame.draw.circle(self.window, GREY, (WIDTH//2, i), circle_radius)

            # pygame.draw.rect(
            #     self.window, self.WHITE, (self.window_width//2 - 5, i, 10, self.window_height//20))

    def handle_collision(self):
        ball = self.ball
        left_paddle = self.left_paddle
        right_paddle = self.right_paddle

        if ball.y + ball.RADIUS >= self.window_height:
            ball.y_vel *= -1  # reverse the y velocity
        elif ball.y - ball.RADIUS <= 0:
            ball.y_vel *= -1

        if ball.x_vel < 0:
            if ball.y >= left_paddle.y and ball.y <= left_paddle.y + Paddle.HEIGHT:
                if ball.x - ball.RADIUS <= left_paddle.x + Paddle.WIDTH:
                    ball.x_vel *= -1

                    middle_y = left_paddle.y + Paddle.HEIGHT / 2
                    difference_in_y = middle_y - ball.y
                    reduction_factor = (Paddle.HEIGHT / 2) / ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel
                    self.left_hit_count += 1

        else:
            if ball.y >= right_paddle.y and ball.y <= right_paddle.y + Paddle.HEIGHT:
                if ball.x + ball.RADIUS >= right_paddle.x:
                    ball.x_vel *= -1

                    middle_y = right_paddle.y + Paddle.HEIGHT / 2
                    difference_in_y = middle_y - ball.y
                    reduction_factor = (Paddle.HEIGHT / 2) / ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel
                    self.right_hit_count += 1

    # draws the window and all the objects in the window

    def draw_window(self, draw_score=True, draw_hit_count=False):
        self.window.fill(BLACK)  # fills the window with black

        self.draw_divider()

        if draw_score:
            self._draw_score()

        if draw_hit_count:
            self._draw_hit_count()

        for paddle in [self.left_paddle, self.right_paddle]:
            paddle.draw(self.window)

        self.ball.draw(self.window)

    def paddle_movement(self, left=True, up=True):
        # left, right = True returns a boolean value if a movement key is pressed
        if left:
            if up and self.left_paddle.y - Paddle.VEL < 0:
                return False
            if not up and self.left_paddle.y + Paddle.HEIGHT > self.window_height:
                return False
            self.left_paddle.move(up)
        else:
            if up and self.right_paddle.y - Paddle.VEL < 0:
                return False
            if not up and self.right_paddle.y + Paddle.HEIGHT > self.window_height:
                return False
            self.right_paddle.move(up)
        return True

    def game_loop(self):
        self.ball.move()
        self._handle_collision()

        if self.ball.x <= 0:  # if the ball goes past the left paddle, right side scores
            self.ball.reset()
            self.right_score += 1
        elif self.ball.x >= self.window_width:  # if the ball goes past the right paddle, left side scores
            self.ball.reset()
            self.left_score += 1

        game_info = GameInfo(
            self.left_hit_count, self.right_hit_count, self.left_score, self.right_score)

        return game_info

    def reset(self):
        self.ball.reset()
        self.left_paddle.reset()
        self.right_paddle.reset()
        self.left_score = 0
        self.right_score = 0
        self.left_hit_count = 0
        self.right_hit_count = 0
