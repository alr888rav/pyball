import pygame


class Sounds:
    def __init__(self):
        pygame.mixer.music.load('sounds/music.ogg')
        self.ball_sound = pygame.mixer.Sound("sounds/ball.ogg")
        self.win_sound = pygame.mixer.Sound("sounds/win.ogg")
        self.lose_sound = pygame.mixer.Sound("sounds/lose.ogg")
        self.goal_sound = pygame.mixer.Sound("sounds/goal.ogg")
        self.click_sound = pygame.mixer.Sound("sounds/click.ogg")

    def music(self):
        #pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()

    def ball(self):
        self.ball_sound.play()

    def win(self):
        self.win_sound.play()

    def lose(self):
        self.lose_sound.play()

    def goal(self):
        self.goal_sound.play()

    def click(self):
        self.click_sound.play()
