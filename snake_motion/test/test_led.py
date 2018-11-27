#!/usr/bin/python
import RPi.GPIO as gpio
from time import sleep


class Shifter():
    """
        Classe para setar o valor de um shift register.
        Adaptado de:
            https://www.instructables.com/id/Using-a-shift-register-with-Raspberry-Pi/
    """

    inputs = [7, 11, 13, 15, 19, 21, 23, 29, 31, 33, 35, 37]
    clocks = [12, 16, 18, 22]
    clears = [24, 26, 32, 36]

    def __init__(self):
        self.setupBoard()

    def tick(self):
        for clock in self.clocks:
            gpio.output(clock, gpio.HIGH)
        sleep(0.5)
        for clock in self.clocks:
            gpio.output(clock, gpio.LOW)
        sleep(0.5)

    def setValues(self, value):
        for i in range(24):
            for input in self.inputs:
                bitwise = 0x800000 >> i
                bit = bitwise & value
                if(bit == 0):
                    print("Output LOW")
                    gpio.output(input, gpio.LOW)
                else:
                    print("Output HIGH")
                    gpio.output(input, gpio.HIGH)
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
            sleep(0.5)
            shifter.setValues(0x0AAAAAA)
            shifter.clear()
            shifter.setValues(0x0555555)
            shifter.clear()
        except KeyboardInterrupt:
            gpio.cleanup()
            running = False


if __name__ == "__main__":
    main()
