
class missile:

    def __init__(self, xcord, ycord):
        self.x = xcord
        self.y = ycord
    shot = []
    shot2 = []


class mis1(missile):

    def __init__(self, xcord, ycord):
        self.vel = 1
        missile.__init__(self, xcord, ycord)


class mis2(missile):

    def __init__(self, xcord, ycord):
        self.vel = 2
        missile.__init__(self, xcord, ycord)
