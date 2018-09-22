import numpy as np


class Snake:
    """
    Classe representando a cobra.
    """

    def __init__(self):
        print("Cobra criada")


class Game:
    """
    Classe que representa o jogo e seu tabuleiro.
    O tabuleiro corresponde a uma matriz 4x4x4.

    """
    __running = False
    __speed = 1
    __board = None
    __snake = None

    def __init__(self):
        # Cria uma matriz 4x4x4 preenchida com 0s (ver manipulação na biblioteca numpy)
        self.__board = np.zeros((4, 4, 4))
        self.__running = False
        self.__speed = 1
        self.snake = Snake()

    def start_game(self):
        self.__running = True

    def increase_speed(self):
        self.__speed += 1

    def is_game_on(self):
        return self.__running

    def get_board(self):
        return self.__board
