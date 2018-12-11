import os, sys
lib_path = os.path.abspath('../outputs')
sys.path.insert(0,lib_path)

import numpy as np
from gpio_manager import GPIO_Manager
from mouse import Mouse
from fruit import Fruit
from snake import Snake
from tick import Tick

from time import sleep

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

    # Game dinamics components
    __add_tail = False

    def __init__(self):
        # Cria uma matriz 6x4x4 preenchida com 0s (ver manipulação na biblioteca numpy)
        self.__board = [[[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]],
                        [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]],
                        [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]],
                        [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]],
                        [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]],
                        [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]]

        self.__gpio_manager = GPIO_Manager()
        self.__snake = Snake()
        self.__fruit = Fruit()
        self.__mouse = Mouse(self.on_click)

        Tick(self)


    def setTick(self, tick):
        self.__tick = tick


    def on_click(self, isLeft):
        self.__snake.update_direction(isLeft)


    def on_tick(self, tick_count):
        # Executes block every 4 ticks
        if tick_count == 0:
            # Updates snake position (and maybe, adds tail)
            self.__snake.update_position(self.__add_tail)
            if self.__add_tail == True:
                self.__add_tail = False
            # Updates fruit position and snake velocity
            self.update_fruit()
        elif tick_count == 1:
            snake_head = self.__snake.get_head_position()
            snake_tail = self.__snake.get_tail_position()

            self.__board[self.__fruit.face][self.__fruit.col][self.__fruit.lin] = 1
            self.__board[snake_head[0]][snake_head[1]][snake_head[2]] = 1
            self.printBoard()
            self.__gpio_manager.setFaces(self.__board)
            self.__board[snake_tail[0]][snake_tail[1]][snake_tail[2]] = 0
        elif tick_count == 2:
            self.__board[self.__fruit.face][self.__fruit.col][self.__fruit.lin] = 0
            self.printBoard()
            self.__gpio_manager.setFaces(self.__board)


    def update_fruit(self):
        snake_head = self.__snake.get_head_position()
        if self.__fruit.has_been_eaten(snake_head[0], snake_head[1], snake_head[2]):
            self.__board[self.__fruit.face][self.__fruit.col][self.__fruit.lin] = 0
            self.__tick.increase_velocity()
            self.__add_tail = True
            self.__fruit = Fruit()

    def printBoard(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        for i in range(0, 4):
            print('            ', end='')
            print(self.__board[4][i], end='')
            print('')
        for i in range(0, 4):
            for j in range(0, 4):
                print(self.__board[j][i], end='')
            print('')
        for i in range(0, 4):
            print('            ', end='')
            print(self.__board[5][i], end='')
            print('')
        snake_head = self.__snake.get_head_position()

def main():
    game = Game()
    running = True
    while running:
        try:
            1
        except KeyboardInterrupt:
            self.__gpio_manager.clear()
            self.__mouse.finalize()
            running = False

if __name__ == "__main__":
    main()
