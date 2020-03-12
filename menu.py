import pygame
from consts import *


class Menu:
    TEXT_COLOR = pygame.color.THECOLORS['white']
    BORDER_COLOR = pygame.color.THECOLORS['white']
    BG_COLOR = pygame.color.THECOLORS['orange']
    MENU_TEXT = ['Играть', 'Выход']
    MENU_PLAY = 1
    MENU_EXIT = 2

    def __init__(self):
        self.menu_rect = []
        for t in Menu.MENU_TEXT:
            self.menu_rect.append(pygame.Rect(0,0,0,0))
        first_top = SCREEN_HEIGHT / 3
        first_left = SCREEN_WIDTH / 4
        step = SCREEN_HEIGHT / 6
        self.menu_rect[0] = pygame.Rect(first_left, first_top, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 8)
        for i in range(1, len(Menu.MENU_TEXT)):
            self.menu_rect[i] = self.menu_rect[i-1].copy()
            self.menu_rect[i].top = self.menu_rect[i-1].top + step

        max_text = Menu.MENU_TEXT[0]
        for menu in self.menu_rect:
            if len(menu) > len(max_text):
                max_text = menu
        self.font_size = self.font_size(self.menu_rect[0].width, max_text)

    def test(self, x, y):
        if self.menu_rect[0].collidepoint(x, y):
            return Menu.MENU_PLAY
        elif self.menu_rect[1].collidepoint(x, y):
            return Menu.MENU_EXIT
        else:
            return 0

    def font_size(self, width, text):
        text_width = 0
        n = 10
        while text_width < 0.5 * width:
            font = pygame.font.Font('freesansbold.ttf', int(n))
            text_width, text_height = font.size(text)
            n += 2
        return n

    def draw(self, screen):

        for i in range(len(Menu.MENU_TEXT)):
            # bg, border
            rect_surface = pygame.Surface((self.menu_rect[i].width, self.menu_rect[i].height))
            rect_surface.fill(Menu.BG_COLOR)
            #pygame.draw.rect(rect_surface, Menu.BORDER_COLOR, rect_surface.get_rect(), 1)
            # text
            font = pygame.font.Font('freesansbold.ttf', self.font_size)
            text_surface = font.render(Menu.MENU_TEXT[i], True, Menu.TEXT_COLOR)
            text_rect = text_surface.get_rect()
            text_rect.center = self.menu_rect[i].center
            # draw
            screen.blit(rect_surface, self.menu_rect[i])
            screen.blit(text_surface, text_rect)
