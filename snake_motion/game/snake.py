from enum import Enum
from enum import IntEnum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Face(IntEnum):
    FRONT = 0
    TOP = 1
    BACK = 2
    DOWN = 3
    LEFT = 4
    RIGHT = 5

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


    def move_to_direction():
        if self.__direction == Direction.NORTH:
            self.__lin += 1
        elif self.direction == Direction.EAST:
            self.__col -= 1
        elif self.direction == Direction.WEST:
            self.__col += 1
        elif self.direction == Direction.SOUTH:
            self.__lin -= 1


    def move_to_upper_cube():

        # Column keeps adding and rotating
        if self.__face < Face.DOWN:
            self.__face += 1
            self.__col = 0
        elif self.__face == Face.DOWN:
            self.__face = Face.FRONT
            self.__col = 0

        # Column swaps with line, and now line will add
        elif self.__face == Face.LEFT:
            self.__face = Face.FRONT
            self.__direction = Direction.WEST
            self.__col = self.__lin
            self.__lin = 0
        elif self.__face == Face.RIGHT:
            self.__face = Face.BACK
            self.__direction = Direction.WEST
            self.__col = self.__lin
            self.__lin = 0


    def move_to_lower_cube():

        # Column swaps with line, and now line will subtract
        if self.__face == Face.RIGHT:
            self.__face = Face.FRONT
            self.__direction = Face.EAST
            self.__col = 3 - self.__lin
            self.__lin = 3
        elif self.__face == Face.LEFT:
            self.__face = Face.BACK
            self.__direction = Face.EAST
            self.__col = 3 - self.__lin
            self.__lin = 3

        # Column keeps subtracting and rotating
        elif self.__face == Face.FRONT:
            self.__face = Face.DOWN
            self.__col = 3
        elif self.__face > Face.FRONT:
            self.__face -= 1
            self.__col = 3


    def move_to_left_cube():

        if self.__face == Face.FRONT:
            self.__face = Face.LEFT
            self.__direction = Direction.SOUTH
            self.__lin = self.__col
            self.__col = 3
        elif self.__face == Face.TOP:
            self.__face = Face.LEFT
            # self.__direction = Direction.EAST (redundant)
            self.__col = 3 - self.__col
            self.__lin = 3
        elif self.__face == Face.BACK:
            self.__face = Face.LEFT
            self.__direction = Direction.NORTH
            self.__lin = 3 - self.__col
            self.__col = 0
        elif self.__face == Face.DOWN:
            self.__face = Face.LEFT
            self.__direction = Direction.WEST
            self.__lin = 0
        elif self.__face == Face.LEFT:
            self.__face = Face.DOWN
            self.__direction = Direction.WEST
            self.__lin = 0
        elif self.__face == Face.RIGHT:
            self.__face = Face.TOP
            # self.__direction = Direction.EAST (redundant)
            self.__col = 3 - self.__col
            self.__lin = 3

    def move_to_right_cube():

        if self.__face == Face.FRONT:
            self.__face = Face.RIGHT
            self.__direction = Direction.SOUTH
            self.__lin = 3 - self.__col
            self.__col = 3
        elif self.__face == Face.TOP:
            self.__face = Face.RIGHT
            # self.__direction = Direction.WEST (redundant)
            self.__col = 3 - self.__col
            self.__lin = 0
        elif self.__face == Face.BACK:
            self.__face = Face.RIGHT
            self.__direction = Direction.NORTH
            self.__lin = self.__col
            self.__col = 0
        elif self.__face == Face.DOWN:
            self.__face = Face.RIGHT
            self.__direction = Direction.EAST
            self.__lin = 3
        elif self.__face == Face.RIGHT:
            self.__face = Face.DOWN
            self.__direction = Direction.EAST
            self.__lin = 3
        elif self.__face == Face.LEFT:
            self.__face = Face.TOP
            # self.__direction = Direction.WEST (redundant)
            self.__col = 3 - self.__col
            self.__lin = 0

    def update_position(add_tail):
        """
        Igual a updatePosition de SnakePart, mas precisa definir a posição da
        cabeça com base na direção atual
        """
        if self.__nextPart != None:
            self.__nextPart.update_position(self.__lin, self.__col, self.__face, add_tail)
        else:
            move_to_direction()
            if self.__col > 3:
                move_to_upper_cube()
            if self.__col < 0:
                move_to_lower_cube()
            if self.__lin < 0:
                move_to_left_cube()
            if self.__lin > 3:
                move_to_right_cube()


    def get_head_position():
        return (self.__lin, self.__col, self.__face)
