import pygame as pyg

class Particle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xVel = 4
        self.yVel = 4
        self.time = 0

    def draw(self, gameWindow):
        self.time += 1
        if self.time < 28:
            self.x += self.xVel
            self.y += self.yVel
            pyg.draw.circle(gameWindow, (255, 187, 4), (self.x, self.y), 18)
