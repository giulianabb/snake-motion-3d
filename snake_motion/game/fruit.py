import random

class Fruit:

    __lin = 0
    __col = 0
    __face = 0

    def __init__(self):
        self.__lin = random.randint(0, 3)
        self.__col = random.randint(0, 3)
        self.__face = random.randint(0, 5)

    def has_been_eaten(self, slin, scol, sface):
        return slin == self.__lin and scol == self.__col and sface == self.__face
