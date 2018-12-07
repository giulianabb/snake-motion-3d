import os, sys
lib_path = os.path.abspath('../game')
sys.path.insert(0,lib_path)

from snake import Face
from time import sleep
import RPi.GPIO as gpio
import numpy as np

class GPIO_Manager:
    """
    Classe responsável por controlar as GPIOs
    """

    __view = np.zeros((12, 8))
    __inputs = [7, 11, 13, 15, 19, 21, 23, 29, 31, 33, 35, 37]
    __clocks = [12, 16, 18, 22]
    __clears = [24, 26, 32, 36]

    def __init__(self):
        self.setupBoard()

    def tick(self):
        for clock in self.__clocks:
            gpio.output(clock, gpio.HIGH)
        sleep(0.0001)
        for clock in self.__clocks:
            gpio.output(clock, gpio.LOW)
        sleep(0.0001)

    def setFaces(self, faces):
        self.__view[0] = np.concatenate((
            faces[Face.TOP][3], np.flip(faces[Face.TOP][2], 0)
        ), axis = None)

        self.__view[1] = np.concatenate((
            faces[Face.TOP][1], np.flip(faces[Face.TOP][0], 0)
        ), axis = None)

        self.__view[2] = np.concatenate((
            np.flip(np.transpose(faces[Face.RIGHT])[2], 0), np.transpose(faces[Face.RIGHT])[3]
        ), axis = None)

        self.__view[3] = np.concatenate((
            np.flip(faces[Face.FRONT][0], 0), faces[Face.FRONT][1]
        ), axis = None)

        self.__view[4] = np.concatenate((
            np.transpose(faces[Face.LEFT])[1], np.flip(np.transpose(faces[Face.LEFT])[0], 0)
        ), axis = None)

        self.__view[5] = np.concatenate((
            faces[Face.BACK][3], np.flip(faces[Face.BACK][2], 0)
        ), axis = None)

        self.__view[6] = np.concatenate((
            np.flip(faces[Face.FRONT][2], 0), faces[Face.FRONT][3]
        ), axis = None)

        self.__view[7] = np.concatenate((
            np.transpose(faces[Face.LEFT])[3], np.flip(np.transpose(faces[Face.LEFT])[2], 0)
        ), axis = None)

        self.__view[8] = np.concatenate((
            faces[Face.BACK][1], np.flip(faces[Face.BACK][0], 0)
        ), axis = None)

        self.__view[9] = np.concatenate((
            np.flip(np.transpose(faces[Face.RIGHT])[0], 0), np.transpose(faces[Face.RIGHT])[1]
        ), axis = None)

        self.__view[10] = np.concatenate((
            faces[Face.DOWN][3], np.flip(faces[Face.DOWN][2], 0)
        ), axis = None)

        self.__view[11] = np.concatenate((
            faces[Face.DOWN][1], np.flip(faces[Face.DOWN][0], 0)
        ), axis = None)

        self.showView()

    def showView(self):
        for i in range(8):
            for j in range(12):
                if(self.__view[j][i] == 0):
                    gpio.output(self.__inputs[j], gpio.LOW)
                else:
                    gpio.output(self.__inputs[j], gpio.HIGH)
            self.tick()

    def clear(self):
        for clear in self.__clears:
            gpio.output(clear, gpio.LOW)
        for clock in self.__clocks:
            self.tick()
        for clear in self.__clears:
            gpio.output(clear, gpio.HIGH)

    def setupBoard(self):
        gpio.setmode(gpio.BOARD)
        for input in self.__inputs:
            gpio.setup(input, gpio.OUT)
            gpio.output(input, gpio.LOW)

        for clock in self.__clocks:
            gpio.setup(clock, gpio.OUT)
            gpio.output(clock, gpio.LOW)

        for clear in self.__clears:
            gpio.setup(clear, gpio.OUT)
            gpio.output(clear, gpio.HIGH)
