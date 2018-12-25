win_ht = 700


class spaceship:

    def __init__(self):
        self.y = win_ht * 0.9
        self.x = 300

    def moveleft(self):
        self.x -= 100

    def moveright(self):
        self.x += 100
