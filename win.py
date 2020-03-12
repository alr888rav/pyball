import pygame
from consts import *


class Win:
    TEXT_COLOR = pygame.color.THECOLORS['white']
    BORDER_COLOR = pygame.color.THECOLORS['white']
    BG_COLOR = pygame.color.THECOLORS['red']
    WIDTH = 200
    HEIGHT = 100
    STEP = 1
    TEXT = 'You win !!!'

    def __init__(self, time):
        self._time = time
        self.play = True
        self.image = pygame.Surface((Win.WIDTH, Win.HEIGHT), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.font_size = self.font_size()

    def font_size(self):
        text_width = 0
        n = 10
        while text_width < 0.85 * Win.WIDTH:
            font = pygame.font.Font('freesansbold.ttf', int(n))
            text_width, text_height = font.size(Win.TEXT)
            n += 2
        return n

    def update(self):
        if self.play:
            self._time -= 1
            if self._time <= 0:
                self._time = 0
                self.play = False
        return self._time

    def draw(self, screen):
        if self._time == 0:
            return

        # bg, border
        rect_surface = pygame.Surface((Win.WIDTH, Win.HEIGHT))
        rect_surface.fill(Win.BG_COLOR)
        pygame.draw.rect(rect_surface, Win.BORDER_COLOR, rect_surface.get_rect(), 2)
        # text
        font = pygame.font.Font('freesansbold.ttf', self.font_size)
        text_surface = font.render(self.TEXT, True, Win.TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.image.get_width() / 2, self.image.get_height() / 2)
        # draw
        self.image.blit(rect_surface, rect_surface.get_rect())
        self.image.blit(text_surface, text_rect)
        screen.blit(self.image, self.rect)
