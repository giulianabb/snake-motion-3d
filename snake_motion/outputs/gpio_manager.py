import time
import numpy as np
import RPi.GPIO as GPIO

class GPIO_Manager:
    """
    Classe responsável por controlar as GPIOs
    """

    __serial_pins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    __clock = 13
    __clear = 14

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

        for pin in range(0, 12, 1):
            GPIO.setup(pin, GPIO.OUT)

        GPIO.setup(self.__clock, GPIO.OUT)
        GPIO.setup(self.__clear, GPIO.OUT)


    def draw_cube(self, board):
        parts = []
        for face in range(0, 6, 1):
            self.draw_section(np.array([
                board[face][0], board[face][1]
            ]))
            self.draw_section(np.array([
                board[face][2], board[face][3]
            ]))


    def draw_section(self, section):
        for pixel in range(0, 8, 1):
            GPIO.output(self.__clock, GPIO.LOW)
            GPIO.output(self.__serial_pins[pixel], section[pixel])
            time.sleep(0.001)
            GPIO.output(self.__clock, GPIO.HIGH)
            time.sleep(0.001)
