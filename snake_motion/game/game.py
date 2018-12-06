import os, sys
lib_path = os.path.abspath('../outputs')
sys.path.insert(0,lib_path)

import numpy as np
from gpio_manager import GPIO_Manager
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

    # Animation control components
    __blink_fruit = True

    # Game dinamics components
    __add_tail = False

    def __init__(self):
        # Cria uma matriz 6x4x4 preenchida com 0s (ver manipulação na biblioteca numpy)
        self.__board = np.zeros((6, 4, 4))
        self.__tick = Tick(self.on_tick)
        self.__snake = Snake()
        self.__fruit = Fruit()

    def on_tick(self, tick_count):

        # Executes block every tick
        self.__blink_fruit = not self.__blink_fruit

        # Executes block every 4 ticks
        if tick_count == 0:
            # Updates snake position (and maybe, adds tail)
            self.__snake.update_position(self.__add_tail)
            if self.__add_tail == True:
                self.__add_tail = False
            # Updates fruit position and snake velocity
            self.update_fruit()

    def update_fruit():
        snake_head = self.__snake.get_head_position()
        if self.__fruit.has_been_eaten(snake_head[0], snake_head[1], snake_head[2]):
            self.__tick.increase_velocity()
            self.__add_tail = True
            self.__fruit = Fruit()


def main():
    gpio_manager = GPIO_Manager()
    running = True

    faces = [[[1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 1, 1, 1]],
             [[1, 1, 1, 1],
              [1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 1, 1, 1]],
             [[1, 1, 1, 1],
              [1, 0, 0, 1],
              [1, 0, 0, 1],
              [1, 1, 1, 1]],
             [[1, 1, 1, 1],
              [1, 0, 1, 1],
              [1, 0, 1, 1],
              [1, 1, 1, 1]],
             [[0, 1, 1, 0],
              [1, 0, 0, 1],
              [1, 0, 0, 0],
              [1, 1, 1, 1]],
             [[0, 1, 1, 0],
              [1, 0, 0, 1],
              [1, 0, 0, 1],
              [0, 1, 1, 0]]]

    while running:
        try:
            gpio_manager.setFaces(faces)
            sleep(1.0)
            gpio_manager.clear()

        except KeyboardInterrupt:
            gpio_manager.clear()
            running = False


if __name__ == "__main__":
    main()
