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
            faces[1][0], np.flip(faces[1][1], 0)
        ), axis = None)

        self.__view[1] = np.concatenate((
            faces[1][2], np.flip(faces[1][3], 0)
        ), axis = None)

        self.__view[2] = np.concatenate((
            faces[0][0], np.flip(faces[0][1], 0)
        ), axis = None)

        self.__view[3] = np.concatenate((
            faces[5][2], np.flip(faces[5][3], 0)
        ), axis = None)

        self.__view[4] = np.concatenate((
            faces[4][2], np.flip(faces[4][3], 0)
        ), axis = None)

        self.__view[5] = np.concatenate((
            faces[2][2], np.flip(faces[2][3], 0)
        ), axis = None)

        self.__view[6] = np.concatenate((
            faces[5][1], np.flip(faces[5][0], 0)
        ), axis = None)

        self.__view[7] = np.concatenate((
            faces[4][1], np.flip(faces[4][0], 0)
        ), axis = None)

        self.__view[8] = np.concatenate((
            faces[2][1], np.flip(faces[2][0], 0)
        ), axis = None)

        self.__view[9] = np.concatenate((
            faces[0][3], np.flip(faces[0][2], 0)
        ), axis = None)

        self.__view[10] = np.concatenate((
            faces[3][0], np.flip(faces[3][1], 0)
        ), axis = None)

        self.__view[11] = np.concatenate((
            faces[3][3], np.flip(faces[3][2], 0)
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
