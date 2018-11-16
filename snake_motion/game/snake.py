from enum import Enum
from enum import IntEnum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

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
    __nextPart = None

    def __init__(self, lin, col, face):
        self.__lin = lin
        self.__col = col
        self.__face = face

    def update_position(lin, col, face, add_tail):
        """
        Atualiza a posição dessa parte da cobra, e atualiza a próxima com ela
        Antes:  [3][2][1][Head][ ]
        Depois: [ ][3][2][1][Head]
        """
        if self.__nextPart != None:
            self.__nextPart.update_position(self.__lin, self.__col, self.__face, add_tail)
        elif add_tail == True:
            self.__nextPart = SnakePart(self.__lin, self.__col, self.__face)
        # The update itself
        self.__lin = lin
        self.__col = col
        self.__face = face

class Snake(SnakePart):
    """
    Classe que representa a cobra.
    """
    __direction = Direction.NORTH

    def __init__(self):
        super().__init__(2, 2, 0)
        __nextPart = SnakePart(2, 3, 0)

    def update_direction(direction):
        """
        Atualiza a direção
        """
        self.__direction = direction

    def update_position(add_tail):
        """
        Igual a updatePosition de SnakePart, mas precisa definir a posição da
        cabeça com base na direção atual
        """
        if self.__nextPart != None:
            self.__nextPart.update_position(self.__lin, self.__col, self.__face, add_tail)
        else:
            

    def get_head_position():
        return (self.__lin, self.__col, self.__face)
