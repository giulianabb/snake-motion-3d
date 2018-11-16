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
    __nextPart = None

    def __init__(self, lin, col, face):
        self.__lin = lin
        self.__col = col
        self.__face = face

    def updatePosition(lin, col):
        """
        Atualiza a posição dessa parte da cobra, e atualiza a próxima com ela
        Antes:  [3][2][1][Head][ ]
        Depois: [ ][3][2][1][Head]
        """
        if (self.__nextPart != None)
            self.__nextPart.updatePosition(self.__lin, self.__col)
        self.__lin = lin
        self.__col = col

class Snake(SnakePart):
    """
    Classe que representa a cobra.
    """
    __size = 2
    __direction = NORTH

    def __init__(self):
        super().__init__(2, 2, 0)
        __nextPart = SnakePart(2, 3, 0)

    def updateDirection(direction):
        """
        Atualiza a direção
        """
        self.__direction = direction

    def updatePosition(lin, col):
        """
        Igual a updatePosition de SnakePart, mas precisa definir a posição da
        cabeça com base na direção atual
        """
        if (self.__nextPart != None)
            self.__nextPart.updatePosition(self.__lin, self.__col)
        #TODO: Criar codigo de posicao com base na direcao
