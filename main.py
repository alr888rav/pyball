import os
import sys
import pygame
from pygame.locals import *
from game import Game
from consts import *

def update():
    pass

#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Football")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

game = Game()

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP or event.type == K_w:
                game.key_up(True)
            elif event.key == K_DOWN or event.type == K_s:
                game.key_down(True)
        if event.type == pygame.KEYUP:
            if event.key == K_UP or event.type == K_w:
                game.key_up(False)
            elif event.key == K_DOWN or event.type == K_s:
                game.key_down(False)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            game.mouse = event.pos

    if game.status == Game.EXIT:
        sys.exit()

    game.update()
    game.draw(screen)

    clock.tick(60)
    pygame.display.update()
