import pygame
from players import Player


class Robot(Player):
    NONE = 0
    UP = 1
    DOWN = 2

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/robot_player.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self._rect = self.image.get_rect()
        self._speed = [0, -1]
        self.level = 1

    def ai(self, ball):
        if self.level == 1:
            self.ai1(ball)

    def ai1(self, ball):
        if ball.rect.center[1] > self._rect.bottom:
            self.go_down()
        elif ball.rect.center[1] < self._rect.top:
            self.go_up()
