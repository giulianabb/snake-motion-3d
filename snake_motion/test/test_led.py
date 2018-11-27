#!/usr/bin/python
import RPi.GPIO as gpio
from time import sleep


class Shifter():
    """
        Classe para setar o valor de um shift register.
        Adaptado de:
            https://www.instructables.com/id/Using-a-shift-register-with-Raspberry-Pi/
    """
    
    inputs = [11, 13, 15, 19, 21, 22, 23, 24, 29, 31, 33, 35]
    clocks = [16, 12, 18, 37]
    clears = [ 7, 26, 32, 36]

    def __init__(self):
        self.setupBoard()
        self.pause = 0.0

    def tick(self, clock):
        gpio.output(clock, gpio.HIGH)
        sleep(self.pause)
        gpio.output(clock, gpio.LOW)
        sleep(self.pause)

    def setValue(self, value, clock, input):
        for i in range(24):
            bitwise = 0x800000 >> i
            bit = bitwise & value
            if(bit == 0):
                print("Output LOW")
                gpio.output(input, gpio.LOW)
            else:
                print("Output HIGH")
                gpio.output(input, gpio.HIGH)
            self.tick(clock)

    def clear(self):
        for clear in self.clears:
            gpio.output(clear, gpio.LOW)
        for clock in self.clocks:
            self.tick(clock)
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
            shifter.clear()
            shifter.setValue(0x0AAAAAA, shifter.inputs[0], shifter.clocks[0])
            shifter.setValue(0x0AAAAAA, shifter.inputs[1], shifter.clocks[0])
            shifter.setValue(0x0AAAAAA, shifter.inputs[2], shifter.clocks[0])
            shifter.setValue(0x0AAAAAA, shifter.inputs[3], shifter.clocks[1])
            shifter.setValue(0x0AAAAAA, shifter.inputs[4], shifter.clocks[1])
            shifter.setValue(0x0AAAAAA, shifter.inputs[5], shifter.clocks[1])
            shifter.setValue(0x0AAAAAA, shifter.inputs[6], shifter.clocks[2])
            shifter.setValue(0x0AAAAAA, shifter.inputs[7], shifter.clocks[2])
            shifter.setValue(0x0AAAAAA, shifter.inputs[8], shifter.clocks[2])
            shifter.setValue(0x0AAAAAA, shifter.inputs[9], shifter.clocks[3])
            shifter.setValue(0x0AAAAAA, shifter.inputs[10], shifter.clocks[3])
            shifter.setValue(0x0AAAAAA, shifter.inputs[11], shifter.clocks[3])
            sleep(0.5)
            shifter.clear()
            shifter.setValue(0x0555555, shifter.inputs[0], shifter.clocks[0])
            shifter.setValue(0x0555555, shifter.inputs[1], shifter.clocks[0])
            shifter.setValue(0x0555555, shifter.inputs[2], shifter.clocks[0])
            shifter.setValue(0x0555555, shifter.inputs[3], shifter.clocks[1])
            shifter.setValue(0x0555555, shifter.inputs[4], shifter.clocks[1])
            shifter.setValue(0x0555555, shifter.inputs[5], shifter.clocks[1])
            shifter.setValue(0x0555555, shifter.inputs[6], shifter.clocks[2])
            shifter.setValue(0x0555555, shifter.inputs[7], shifter.clocks[2])
            shifter.setValue(0x0555555, shifter.inputs[8], shifter.clocks[2])
            shifter.setValue(0x0555555, shifter.inputs[9], shifter.clocks[3])
            shifter.setValue(0x0555555, shifter.inputs[10], shifter.clocks[3])
            shifter.setValue(0x0555555, shifter.inputs[11], shifter.clocks[3])
            sleep(0.5)
        except KeyboardInterrupt:
            gpio.cleanup()
            running = False


if __name__ == "__main__":
    main()
