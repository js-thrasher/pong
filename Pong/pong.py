import random
from collections import namedtuple
from ball import Ball
from paddle import Paddle
import pygame


def main():
    pygame.init()

    mynt = namedtuple("Constants", ["WIDTH", "HEIGHT", "BORDER", "VELOCITY", "FPS"])
    constants = mynt(1500, 1000, 15, 5, 144)
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.update()

    wcolor = pygame.Color("white")
    ycolor = pygame.Color("yellow")
    bcolor = pygame.Color("black")

    # top
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (constants.WIDTH, constants.BORDER)))
    # left
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (constants.BORDER, constants.HEIGHT)))
    # bottom
    pygame.draw.rect(screen, wcolor,
                     pygame.Rect((0, constants.HEIGHT - constants.BORDER), (constants.WIDTH, constants.HEIGHT)))

    x0 = constants.WIDTH - Ball.RADIUS
    y0 = constants.HEIGHT // 2
    vx0 = constants.VELOCITY * (0.5 - random.random())
    vy0 = constants.VELOCITY * (0.5 - random.random())
    b0 = Ball(x0, y0, vx0, vy0, screen, ycolor, bcolor, constants)
    b0.show(b0.fgcolor)
    pygame.display.update()
    running = True
    clock = pygame.time.Clock()

    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.update()
        clock.tick(constants.FPS)
        b0.update()


if __name__ == "__main__":
    main()
