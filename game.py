import pygame

from Lose import Lose
from balls import Ball
from goal import Goal
from human import Human
from menu import Menu
from robot import Robot
from consts import *
from sounds import Sounds
from win import Win


class Game:
    FPS = 60
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PLAY = 0
    PAUSE = 1
    GOAL = 2
    WIN = 3
    LOSE = 4
    MENU = 5
    EXIT = 6
    GOAL_TIME = 2 * FPS # 2 sec
    WIN_TIME = 3 * FPS
    LOSE_TIME = 3 * FPS
    MAX_SCORE = 3

    def __init__(self):
        self.bg = pygame.image.load("images/bg.jpg")
        self.bg = pygame.transform.scale(self.bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bgrect = self.bg.get_rect()
        self.ball = Ball()
        self.human = Human()
        self.robot = Robot()
        self.goal = Goal(0)
        self.win = Win(0)
        self.lose = Lose(0)
        self.menu = Menu()
        self.mouse = (0,0)
        self.sounds = Sounds()
        self.sounds.music()
        self.status = Game.MENU
        self.reset()

    def reset(self):
        self.ball.set_pos(0.3 * SCREEN_WIDTH, 0.3 * SCREEN_HEIGHT)
        self.human.set_pos(0.05 * SCREEN_WIDTH, SCREEN_HEIGHT / 2 - self.human.height() / 2)
        self.robot.set_pos(0.8 * SCREEN_WIDTH, SCREEN_HEIGHT / 2 - self.robot.height() / 2)
        self.human.score = 0
        self.robot.score = 0
        self.last_detect = 0
        self._key_up = False
        self._key_down = False
        self.status = Game.MENU

    def goal_start(self):
        self.status = Game.GOAL
        self.goal = Goal(Game.GOAL_TIME)

    def win_start(self):
        self.status = Game.WIN
        self.win = Win(Game.WIN_TIME)

    def lose_start(self):
        self.status = Game.LOSE
        self.lose = Lose(Game.LOSE_TIME)

    def update(self):

        if self.status == Game.MENU:
            if self.menu.test(self.mouse[0], self.mouse[1]) == Menu.MENU_PLAY: # menu -> play
                self.reset()
                self.status = Game.PLAY
                self.sounds.click()
            elif self.menu.test(self.mouse[0], self.mouse[1]) == Menu.MENU_EXIT: # menu -> exit
                self.status = Game.EXIT
                self.sounds.click()
        # goal -> continue
        elif self.status == Game.GOAL and self.goal.update() == 0:
            if self.robot.score >= Game.MAX_SCORE: # goal -> end game
                self.lose_start()
                self.sounds.lose()
            elif self.human.score >= Game.MAX_SCORE: # goal -> end game
                self.win_start()
                self.sounds.win()
            else:
                self.status = Game.PLAY # goal -> continue play
        # process win/lose
        elif self.status == Game.WIN:
            if self.win.update() == 0:
                self.status = Game.MENU # win -> menu
        elif self.status == Game.LOSE:
            if self.lose.update() == 0:
                self.status = Game.MENU # lose -> menu
        elif self.status == Game.PLAY:
            # calc next
            self.ball.move()
            if self._key_up and self.human.top() > SCREEN_HEIGHT / 10:
                self.human.go_up()
            elif self._key_down and self.human.bottom() < SCREEN_HEIGHT * 9 / 10:
                self.human.go_down()
            #self.robot.move()
            # goal detect
            if self.ball.left() < 0:
                self.robot.score += 1
                self.ball.reset(SCREEN_WIDTH, SCREEN_HEIGHT)
                self.goal_start()
                self.status = Game.GOAL
                self.sounds.goal()
            # goal detect
            if self.ball.right() > SCREEN_WIDTH:
                self.human.score += 1
                self.ball.reset(SCREEN_WIDTH, SCREEN_HEIGHT)
                self.goal_start()
                self.status = Game.GOAL
                self.sounds.goal()
            # wall collision detect
            if self.ball.top() < 0 or self.ball.bottom() > SCREEN_HEIGHT:
                self.ball.toggleY()
                self.sounds.ball()
            # player collision detect
            if pygame.time.get_ticks() - self.last_detect > 500:
                if self.ball.collision(self.human.rect()) or self.ball.collision(self.robot.rect()):
                    self.last_detect = pygame.time.get_ticks()
                    self.sounds.ball()
            # robot update
            if self.robot.level == 0 and self.robot.top() < SCREEN_HEIGHT / 10 or self.robot.bottom() > SCREEN_HEIGHT * 9 / 10:
                self.robot.toggle_y()
            elif self.robot.level == 1:
                self.robot.ai(self.ball)

        self.mouse = (0,0)

    def draw_score(self, screen):
        text = str(self.human.score) + ' : ' + str(self.robot.score)
        font = pygame.font.Font('freesansbold.ttf', 30)
        text_surface = font.render(text, True, Game.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = ((SCREEN_WIDTH / 2), (0.1 * SCREEN_HEIGHT))
        screen.blit(text_surface, text_rect)

    def draw(self, screen):
        screen.fill(Game.BLACK)
        screen.blit(self.bg, self.bgrect)
        self.ball.draw(screen)
        self.human.draw(screen)
        self.robot.draw(screen)
        self.draw_score(screen)
        self.goal.draw(screen)

        if self.status == Game.MENU:
            self.menu.draw(screen)
        elif self.status == Game.WIN:
            self.win.draw(screen)
        elif self.status == Game.LOSE:
            self.lose.draw(screen)

    def key_up(self, status):
        self._key_up = status

    def key_down(self, status):
        self._key_down = status
