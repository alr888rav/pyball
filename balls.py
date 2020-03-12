import pygame
import random

class Ball:
    COL_NONE = 0
    COL_LEFT = 1
    COL_RIGHT = 2
    COL_TOP = 3
    COL_BOTTOM = 4

    def __init__(self):
        self.image = pygame.image.load("images/ball.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.speed = [2, 1]

    def _sign(self, value):
        if value < 0:
            return -1
        else:
            return 1

    def reset(self, width, height):
        x = random.randint(0.4 * width, 0.6 * width)
        y = random.randint(0.4 * height, 0.6 * height)
        self.set_pos(x, y)

        self.speed[0] *= self._sign(random.randint(-1, 1))
        self.speed[1] *= self._sign(random.randint(-1, 1))

    def center(self):
        return self.rect.center[0]

    def left(self):
        return self.rect.left

    def right(self):
        return self.rect.right

    def top(self):
        return self.rect.top

    def bottom(self):
        return self.rect.bottom

    def move(self):
        self.rect = self.rect.move(self.speed)

    def toggleX(self):
        self.speed[0] = -self.speed[0]

    def toggleY(self):
        self.speed[1] = -self.speed[1]
        
    def collision(self, rect):
        res = False
        if rect.collidepoint(self.rect.midtop) or rect.collidepoint(self.rect.midbottom):
            self.speed[1] = -self.speed[1]
            res = True
        if rect.collidepoint(self.rect.midleft) or rect.collidepoint(self.rect.midright):
            self.speed[0] = -self.speed[0]
            res = True
        return res

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def set_pos(self, x, y):
        self.rect.left = 0
        self.rect.top = 0
        self.rect = self.rect.move(x, y)

    def get_pos(self):
        return self.rect