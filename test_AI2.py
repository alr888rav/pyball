from unittest import TestCase
from ai2 import AI2
from balls import Ball
from consts import *
from robot import Robot


class TestAI2(TestCase):

    def test_act(self):
        ai2 = AI2()
        ai2.train()
        # tests
        b = [(100, 100), (100, 100), (100, 100), (100, 100), (100, 100)]
        s = [(1, 1), (1, 1), (1, 1), (1, -1), (-1, -1)]
        r = [(200, 50), (200, 100), (200, 50), (200, 50), (200, 50)]
        a = [DOWN, NONE, DOWN, DOWN, NONE]
        # test 1 -> DOWN
        ball = Ball()
        rb = Robot()
        for i in range(len(b)):
            ball.set_pos(b[i][0], b[i][1])
            ball.speed = [s[i][0], s[i][1]]
            rb.set_pos(r[i][0], r[i][1])
            act = ai2.action(ball, rb)
            assert act == a[i], str(i) + ' not passed'

