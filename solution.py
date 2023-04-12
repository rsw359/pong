import pygame

pygame.init()  # initializes pygame

WHITE = (255, 255, 255)  # sets the color white
BLACK = (0, 0, 0)  # sets the color black
FPS = 60  # sets the fps of the game
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # sets the size of the window
pygame.display.set_caption("Pong!")  # sets the title of the window

PADDLE_HEIGHT, PADDLE_WIDTH = 20, 100


class Paddle:
    COLOR = WHITE

    def __init__(self, x, y, width, height):  # initializes the paddle
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        def draw(self, win):  # draws the paddle
            pygame.draw.rectangle(
                win, self.COLOR, (self.x, self.y, self.width, self.height)
            )


def draw_window(win):  # draws the window
    win.fill(BLACK)  # fills the window with black
    # updates the window with the new changes in this window function
    pygame.display.update()


# event loop
def main():
    run = True
    # creates a clock object that determines the fps of the game
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    draw_window(WIN)
    while run:  # main loop that runs the game
        clock.tick(FPS)  # sets the fps of the game, cannot go over the fps

        for (event) in pygame.event.get():  # loops through all the events that happen in the game
            if event.type == pygame.QUIT:  # if the event is the user clicking the x button and closes the game
                run = False
                break
    pygame.quit()


if __name__ == "__main__":  # runs the main function
    main()
