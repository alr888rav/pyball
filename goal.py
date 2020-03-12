import pygame
from consts import *

class Goal:
    TEXT_COLOR = pygame.color.THECOLORS['yellow']
    BORDER_COLOR = pygame.color.THECOLORS['white']
    BG_COLOR = pygame.color.THECOLORS['white']
    MIN_SIZE = 5
    MAX_SIZE = 30
    STEP = 0.5

    def __init__(self, time):
        self._time = time
        self._size = Goal.MIN_SIZE
        self.play = True

    def update(self):
        if self.play:
            self._size += Goal.STEP
            if self._size > Goal.MAX_SIZE:
                self._size = Goal.MAX_SIZE
            self._time -= 1
            if self._time <= 0:
                self._time = 0
                self.play = False
        return self._time

    def draw(self, screen):
        if self._time == 0:
            return
        text = 'Goal !!!'
        font = pygame.font.Font('freesansbold.ttf', int(self._size))
        text_surface = font.render(text, True, Goal.TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        screen.blit(text_surface, text_rect)
