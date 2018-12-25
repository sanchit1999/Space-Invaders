from random import randint
win_ht = 700


class alien:

    def __init__(self):
        self.ans = 0
        temp = randint(0, 7)
        self.x = temp * 100
        temp = randint(2, 3)
        self.y = 0.1 * temp * win_ht
    aliens = []
    temp = []
