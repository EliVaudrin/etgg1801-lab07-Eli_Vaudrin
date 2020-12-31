# ETGG 1801
# Eli Vaudrin
# Lab07 Particle Engine
# 11/7/2020

import pygame as pyg
from particleEngine import Particle

pyg.init()

gameWindow = pyg.display.set_mode((1000, 800))

clock = pyg.time.Clock()

isRunning = True
particles = []

while isRunning:

    for evt in pyg.event.get():
        if evt.type == pyg.QUIT:
            isRunning = False
        elif evt.type == pyg.KEYDOWN:
            if evt.key == pyg.K_ESCAPE:
                isRunning = False

    spcBar = pyg.key.get_pressed()
    if spcBar[pyg.K_SPACE]:
        for x in range(27):
            particles.append(Particle(500, 400))


    for Particle in particles:
        Particle.draw(gameWindow)

    pyg.display.update()
    clock.tick() / 1000

pyg.quit()