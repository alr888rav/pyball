import pygame

from ai2 import AI2
from consts import *
from players import Player


class Robot(Player):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/robot_player.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self._rect = self.image.get_rect()
        self._speed = [0, -1]
        self.level = 1
        self.AI = None

    def ai(self, ball):
        if self.level == 1:
            self.ai1(ball)
        elif self.level == 2:
            self.ai2(ball)

    def ai1(self, ball):
        if ball.rect.center[1] > self._rect.bottom:
            self.go_down()
        elif ball.rect.center[1] < self._rect.top:
            self.go_up()

    def ai2(self, ball):
        if self.AI is None:
            self.AI = AI2()
        act = self.AI.action(ball, self)
        if act == UP:
            self.go_up()
        elif act == DOWN:
            self.go_down()