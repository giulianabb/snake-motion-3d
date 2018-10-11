from enum import Enum
from enum import IntEnum

class Direction(Enum):
    NORTH
    EAST
    SOUTH
    WEST

class Face(IntEnum):
    FRONT = 0
    RIGHT = 1
    BACK = 2
    LEFT = 3
    TOP = 4
    DOWN = 5

class SnakePart:

    __lin = 0
    __col = 0
    __face = 0
    __direction = NORTH
    __part = None

    def __init__(self, lin, col, face):
        self.__lin = lin
        self.__col = col
        self.__face = face

    def updateDirection(direction):
        self.__direction = direction

    def updatePosition():
        


class Snake(SnakePart):
    """
    Classe que representa a cobra.
    """
    __size = 2

    def __init__(self):
