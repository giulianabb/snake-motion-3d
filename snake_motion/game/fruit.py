import random

class Fruit:

    lin = 0
    col = 0
    face = 0

    def __init__(self):
        self.lin = random.randint(0, 3)
        self.col = random.randint(0, 3)
        self.face = random.randint(0, 5)

    def has_been_eaten(self, slin, scol, sface):
        return slin == self.lin and scol == self.col and sface == self.face
