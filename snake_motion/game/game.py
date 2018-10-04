import numpy as np
from tick import Tick

class Game:
    """
    Classe que representa o jogo e seu tabuleiro.
    O tabuleiro corresponde a uma matriz 4x4x6.
    """
    # __running = False
    # __speed = 1
    # __board = None
    # __snake = None

    def __init__(self):
        # Cria uma matriz 4x4x6 preenchida com 0s (ver manipulação na biblioteca numpy)
        self.__board = np.zeros((4, 4, 6))
        self.__running = False
        self.__speed = 1

        Tick(self.on_tick)

    def on_tick(self, __tick_count):


    # def start_game(self):
    #     self.__running = True
    #
    # def increase_speed(self):
    #     self.__speed += 1
    #
    # def is_game_on(self):
    #     return self.__running
    #
    # def get_board(self):
    #     return self.__board
