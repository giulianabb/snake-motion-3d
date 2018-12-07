#!/usr/bin/python
import RPi.GPIO as gpio
from time import sleep


class Shifter():
    """
        Classe para setar o valor de um shift register.
        Adaptado de:
            https://www.instructables.com/id/Using-a-shift-register-with-Raspberry-Pi/
    """

    views = [[1, 0, 1, 0, 1, 0, 1, 0],  # C1  TOP
             [0, 1, 0, 1, 0, 1, 0, 1],  # C2  TOP
             [0, 0, 0, 0, 0, 0, 0, 0],  # F1  FRONT
             [0, 0, 0, 0, 0, 0, 0, 0],  # D2  RIGHT
             [0, 0, 0, 0, 0, 0, 0, 0],  # A2  BACK
             [0, 0, 0, 0, 0, 0, 0, 0],  # E2  LEFT
             [0, 0, 0, 0, 0, 0, 0, 0],  # D1  RIGHT
             [0, 0, 0, 0, 0, 0, 0, 0],  # A1  BACK
             [0, 0, 0, 0, 0, 0, 0, 0],  # E1  LEFT
             [0, 0, 0, 0, 0, 0, 0, 0],  # F2  FRONT
             [0, 0, 0, 0, 0, 0, 0, 0],  # B1  DOWN
             [0, 0, 0, 0, 0, 0, 0, 0]]  # B2  DOWN

    inputs = [7, 11, 13, 15, 19, 21, 23, 29, 31, 33, 35, 37]
    clocks = [12, 16, 18, 22]
    clears = [24, 26, 32, 36]

    def __init__(self):
        self.setupBoard()

    def tick(self):
        for clock in self.clocks:
            gpio.output(clock, gpio.HIGH)
        sleep(0.0001)
        for clock in self.clocks:
            gpio.output(clock, gpio.LOW)
        sleep(0.0001)

    def setValues(self, view):
        for i in range(8):
            for j in range(12):
                if(view[j][i] == 0):
                    print("Output LOW")
                    gpio.output(self.inputs[j], gpio.LOW)
                else:
                    print("Output HIGH")
                    gpio.output(self.inputs[j], gpio.HIGH)
            self.tick()

    def clear(self):
        for clear in self.clears:
            gpio.output(clear, gpio.LOW)
        for clock in self.clocks:
            self.tick()
        for clear in self.clears:
            gpio.output(clear, gpio.HIGH)

    def setupBoard(self):
        for input in self.inputs:
            gpio.setup(input, gpio.OUT)
            gpio.output(input, gpio.LOW)

        for clock in self.clocks:
            gpio.setup(clock, gpio.OUT)
            gpio.output(clock, gpio.LOW)

        for clear in self.clears:
            gpio.setup(clear, gpio.OUT)
            gpio.output(clear, gpio.HIGH)

def main():
    gpio.setmode(gpio.BOARD)
    shifter = Shifter()
    running = True
    while running:
        try:
            shifter.setValues(shifter.views)
            sleep(1.0)
            shifter.clear()

        except KeyboardInterrupt:
            shifter.clear()
            gpio.cleanup()
            running = False


if __name__ == "__main__":
    main()
