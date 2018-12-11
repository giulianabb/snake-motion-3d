
from enum import IntEnum

class Direction(IntEnum):
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

    lin = 0
    col = 0
    face = 0
    nextPart = None

    def __init__(self, lin, col, face):
        self.lin = lin
        self.col = col
        self.face = face

    def update_position(self, lin, col, face, add_tail):
        """
        Atualiza a posição dessa parte da cobra, e atualiza a próxima com ela
        Antes:  [3][2][1][Head][ ]
        Depois: [ ][3][2][1][Head]
        """
        if self.nextPart != None:
            self.nextPart.update_position(self.lin, self.col, self.face, add_tail)
        elif add_tail == True:
            self.nextPart = SnakePart(self.lin, self.col, self.face)
        # The update itself
        self.lin = lin
        self.col = col
        self.face = face

    def get_tail_position(self):
        if (self.nextPart == None):
            return (self.face, self.col, self.lin)
        else:
            return self.nextPart.get_tail_position()

class Snake(SnakePart):
    """
    Classe que representa a cobra.
    """
    direction = Direction.WEST

    def __init__(self):
        super().__init__(2, 2, Face.TOP)
        self.nextPart = SnakePart(1, 2, Face.TOP)
        self.nextPart.nextPart = SnakePart(0, 2, Face.TOP)


    def update_direction(self, isClockwise):
        if (isClockwise):
            self.direction = (self.direction - 1) % 4
        else:
            self.direction = (self.direction + 1) % 4

    def move_to_direction(self):
        if self.direction == Direction.NORTH:
            self.col += 1
        elif self.direction == Direction.EAST:
            self.lin -= 1
        elif self.direction == Direction.WEST:
            self.lin += 1
        elif self.direction == Direction.SOUTH:
            self.col -= 1


    def move_to_upper_cube(self):
        if self.face < Face.LEFT:
            self.face = (self.face + 1) % Face.LEFT
            self.col = 0
        else:
            self.face = Face.FRONT if self.face == Face.LEFT else Face.BACK
            self.direction = Direction.WEST
            self.col = self.lin
            self.lin = 0


    def move_to_lower_cube(self):
        if self.face < Face.LEFT:
            self.face = (self.face - 1) % Face.LEFT
            self.col = 3
        else:
            print('ideia errada aqui')
            self.face = Face.FRONT if self.face == Face.LEFT else Face.BACK
            self.direction = Direction.EAST
            self.col = 3 - self.lin
            self.lin = 3


    def move_to_left_cube(self):
        if self.face < Face.LEFT:
            self.direction = (2 - self.face) % Face.LEFT
            if self.face == Face.FRONT:
                self.lin = self.col
                self.col = 3
            elif self.face == Face.TOP:
                self.col = 3 - self.col
                self.lin = 3
            elif self.face == Face.BACK:
                self.lin = 3 - self.col
                self.col = 0
            elif self.face == Face.DOWN:
                self.lin = 0
            self.face = Face.LEFT

        elif self.face == Face.LEFT:
            self.face = Face.DOWN
            self.direction = Direction.WEST
            self.lin = 0
        elif self.face == Face.RIGHT:
            self.face = Face.TOP
            self.col = 3 - self.col
            self.lin = 3


    def move_to_right_cube(self):
        if self.face < Face.LEFT:
            self.direction = (self.face - 2) % Face.LEFT
            if self.face == Face.FRONT:
                self.lin = 3 - self.col
                self.col = 3
            elif self.face == Face.TOP:
                self.col = 3 - self.col
                self.lin = 0
            elif self.face == Face.BACK:
                self.lin = self.col
                self.col = 0
            elif self.face == Face.DOWN:
                self.lin = 3
            self.face = Face.RIGHT

        elif self.face == Face.RIGHT:
            self.face = Face.DOWN
            self.direction = Direction.EAST
            self.lin = 3
        elif self.face == Face.LEFT:
            self.face = Face.TOP
            self.col = 3 - self.col
            self.lin = 0


    def update_position(self, add_tail):
        """
        Igual a updatePosition de SnakePart, mas precisa definir a posição da
        cabeça com base na direção atual
        """
        if self.nextPart != None:
            self.nextPart.update_position(self.lin, self.col, self.face, add_tail)

        self.move_to_direction()
        if self.col > 3:
            self.move_to_upper_cube()
        elif self.col < 0:
            self.move_to_lower_cube()
        elif self.lin < 0:
            self.move_to_left_cube()
        elif self.lin > 3:
            self.move_to_right_cube()


    def get_head_position(self):
        return (self.face, self.col, self.lin)
