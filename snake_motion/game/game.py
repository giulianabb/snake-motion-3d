import numpy as np
from tick import Tick


class Game:
    """
    Classe que representa o jogo e seu tabuleiro.
    O tabuleiro corresponde a uma matriz 6x4x4.
    """

    # Game's key components
    __board = None
    __snake = None
    __fruit = None
    __tick = None

    # Animation control components
    __blink_fruit = True

    def __init__(self):
        # Cria uma matriz 6x4x4 preenchida com 0s (ver manipulação na biblioteca numpy)
        self.__board = np.zeros((6, 4, 4))
        self.__tick = Tick(self.on_tick)
        self.__snake = Snake()
        self.__fruit = Fruit()

    def on_tick(self, tick_count):

        # Blinks the fruits every 1 tick
        self.__blink_fruit = not self.__blink_fruit

        # Updates position every 4 ticks
        if tick_count == 0:
            self.__snake.update_position()
            self.update_fruit()
            

    def update_fruit():
        snake_head = self.__snake.get_head_position()
        if self.__fruit.has_been_eaten(snake_head[0], snake_head[1], snake_head[2]):
            self.__tick.increase_velocity()
            self.__fruit = Fruit()
