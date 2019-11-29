# -*- coding: utf-8 -*-
import pygame


size = width, height = 2000, 1000
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
y = pygame.Color('yellow')
q = 0
while running:
    screen.fill((0, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            q = 1
            raz = 10
            pygame.draw.circle(screen, y, event.pos, raz)
            kek = event.pos
    if q == 0:
        pass
    if q == 1:
        pygame.draw.circle(screen, y, kek, raz)
        raz += 1
    pygame.display.flip()
    clock.tick(50)