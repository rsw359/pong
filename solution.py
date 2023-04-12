import pygame

pygame.init()  # initializes pygame


GREY = (128, 128, 128)
WHITE = (255, 255, 255)  # sets the color white
BLACK = (0, 0, 0)  # sets the color black
FPS = 60  # sets the fps of the game
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # sets the size of the window
pygame.display.set_caption("Pong!")  # sets the title of the window

PADDLE_HEIGHT, PADDLE_WIDTH = 100, 20


class Paddle:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):  # initializes the paddle
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):  # draws the paddle
        pygame.draw.rect(
            win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL  # upward movement subtracts from the velocity, moves the paddle up
        else:
            self.y += self.VEL  # downward movement adds to the velocity, moves the paddle down


def draw_window(win, paddles):  # draws the window and all the objects in the window
    win.fill(BLACK)  # fills the window with blac
    for paddle in paddles:
        paddle.draw(win)

    # Define the color and size of the divider circles
    circle_color = GREY
    circle_radius = HEIGHT // 200

    # Define the spacing between the divider circles
    circle_spacing = circle_radius * 4

    # Loop through the screen height with the given spacing
    for i in range(circle_radius, HEIGHT, circle_spacing):
        # Draw a circle at the current position
        pygame.draw.circle(win, circle_color, (WIDTH//2, i), circle_radius)

    # for i in range(20, HEIGHT, HEIGHT//20):
    #     if i % 2 == 0:
    #         continue
    #     pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))
    # updates the window with the new changes in this window function
    pygame.display.update()


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:  # if the w key is pressed
        left_paddle.move(up=True)  # moves the left paddle up
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:  # if the s key is pressed
        left_paddle.move(up=False)  # moves the left paddle down

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:  # if the up arrow key is pressed
        right_paddle.move(up=True)  # moves the right paddle up
    # if the down arrow key is pressed
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + left_paddle.height <= HEIGHT:
        right_paddle.move(up=False)  # moves the right paddle down


# event loop
def main():
    run = True
    # creates a clock object that determines the fps of the game
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT //
                         2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT //
                          2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    while run:  # main loop that runs the game
        clock.tick(FPS)
        draw_window(WIN, [left_paddle, right_paddle])

        for (event) in pygame.event.get():  # loops through all the events that happen in the game
            if event.type == pygame.QUIT:  # if the event is the user clicking the x button and closes the game
                run = False
                break

        keys = pygame.key.get_pressed()  # gets all the keys that are pressed
        handle_paddle_movement(keys, left_paddle, right_paddle)
    pygame.quit()


if __name__ == "__main__":  # runs the main function
    main()
