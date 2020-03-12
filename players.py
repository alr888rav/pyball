import pygame


class Player:
    def __init__(self):
        pass
        self.image = pygame.image.load("images/default_player.png")
        self._rect = self.image.get_rect()
        self._speed = [0, 0]
        self.score = 0

    def rect(self):
        return self._rect

    def set_pos(self, x, y):
        self._rect.left = 0
        self._rect.top = 0
        self._rect = self._rect.move(x, y)

    def height(self):
        return self._rect.height

    def width(self):
        return self._rect.width

    def left(self):
        return self._rect.left

    def right(self):
        return self._rect.left + self._rect.width

    def top(self):
        return self._rect.top

    def bottom(self):
        return self._rect.top + self._rect.height

    def move(self):
        self._rect = self._rect.move(self._speed)

    def toggle_x(self):
        self._speed[0] = -self._speed[0]

    def toggle_y(self):
        self._speed[1] = -self._speed[1]

    def draw(self, screen):
        screen.blit(self.image, self._rect)

    def go_up(self):
        self._rect = self._rect.move(0, -abs(self._speed[1]))

    def go_down(self):
        self._rect = self._rect.move(0, abs(self._speed[1]))
