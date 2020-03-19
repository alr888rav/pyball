# import tensorflow as tf
from os import path

import keras
from keras.layers import Dense
from keras.models import Sequential
import numpy as np

from consts import *


class AI2:
    MODEL = 'pyball_model.h5'

    def __init__(self):
        self.history = None
        self.loss = None
        self.accuracy = None
        if path.exists(AI2.MODEL):
            self.load()
            self.ready = True
        else:
            self.model = Sequential()
            self.model.add(Dense(16, activation='relu', input_shape=(4,)))   # input ball pos Y, ball speed X,Y, player pos Y
            self.model.add(Dense(8, activation='relu'))
            self.model.add(Dense(4, activation='relu'))
            self.model.add(Dense(3, activation='softmax'))  # out go up/none/down
            self.model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
            self.ready = False

    def train(self):
        # generate training data
        pos_ball = np.arange(0, 5, 1)  # 0-20% 20-40% 40-60% 60-80% 80-100%
        spd_x = [-1, 1]
        spd_y = [-1, 1]
        pos_plr = np.arange(0, 5, 1)  # 0% 25% 50% 75% 100%
        inp = np.zeros((100, 4))  # 5 * 2 * 2 * 5
        out = np.zeros((100, 3))  # out -> up none down
        i = 0
        for pb in pos_ball:
            for spX in spd_x:
                for spY in spd_y:
                    for pp in pos_plr:
                        # input
                        inp[i][0] = pb
                        inp[i][1] = pp
                        inp[i][2] = spX
                        inp[i][3] = spY
                        # output
                        if spX < 0:  # robor -> human
                            out[i][0] = 0
                            out[i][1] = 1
                            out[i][2] = 0
                        else:  # human -> robot
                            if pb < pp:  # up
                                out[i][0] = 1
                                out[i][1] = 0
                                out[i][2] = 0
                            elif pb > pp:  # down
                                out[i][0] = 0
                                out[i][1] = 0
                                out[i][2] = 1
                            else:  # none
                                out[i][0] = 0
                                out[i][1] = 1
                                out[i][2] = 0
                        i += 1

        x_train = inp
        y_train = out
        print("in: \n", x_train[:5])
        print("out: \n", y_train[:5])
        # fit & test
        if not self.ready:
            self.history = self.model.fit(x_train, y_train, epochs=500, verbose=False)
        self.loss, self.accuracy = self.model.evaluate(x_train, y_train, verbose=False)
        print(f'Test accuracy: {self.accuracy:.3}')
        if self.accuracy == 1 and not path.exists(AI2.MODEL):
            self.save()

    @classmethod
    def y_to_category(cls, y):
        if y < 0.2 * SCREEN_HEIGHT:
            return 0
        elif y < 0.4 * SCREEN_HEIGHT:
            return 1
        elif y < 0.6 * SCREEN_HEIGHT:
            return 2
        elif y < 0.8 * SCREEN_HEIGHT:
            return 3
        else:
            return 4

    def action(self, ball, player):
        inp = np.zeros((1, 4))
        inp[0][0] = self.y_to_category(ball.get_pos().center[1])
        inp[0][1] = self.y_to_category(player.get_pos().center[1])
        inp[0][2] = ball.speed[0]
        inp[0][3] = ball.speed[1]
        predictions = self.model.predict(inp)
        if predictions[0][0] >= 0.5:
            return UP
        elif predictions[0][2] >= 0.5:
            return DOWN
        else:
            return NONE

    def save(self):
        self.model.save(AI2.MODEL)

    def load(self):
        self.model = keras.models.load_model(AI2.MODEL)
