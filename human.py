import pygame
from players import Player


class Human(Player):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/human_player.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self._rect = self.image.get_rect()
        self._speed = [0, 1]
