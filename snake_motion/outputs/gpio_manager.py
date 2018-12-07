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
        for i in range(12):
            face_number = int((i - i % 2) / 2)
            face_row = int((i % 2) * 2)
            if (i == 1 or (i >= 6 and i != 10)):
                self.__view[i] = np.concatenate((
                    faces[face_number][face_row + 1],
                    faces[face_number][face_row]),
                    axis = None)
            else:
                self.__view[i] = np.concatenate((
                    faces[face_number][face_row],
                    faces[face_number][face_row + 1]),
                    axis = None)
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
