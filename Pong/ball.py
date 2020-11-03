import pygame


class Ball:
    RADIUS = 10

    def __init__(self, x, y, vx, vy, screen, fgcolor, bgcolor, constants):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.screen = screen
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.constants = constants

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        self.show(self.bgcolor)
        px = self.x + self.vx
        py = self.y + self.vy
        if px < (self.constants.BORDER + self.RADIUS):
            self.vx = -self.vx
        if (py < self.constants.BORDER + self.RADIUS) or (py > self.constants.HEIGHT - (self.constants.BORDER + self.RADIUS)):
            self.vy = -self.vy
        self.x += self.vx
        self.y += self.vy
        self.show(self.fgcolor)
