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
        self.pause = 0.5

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
            shifter.setValue(0x0AAAAAA, self.inputs[0], self.clocks[0])
            shifter.setValue(0x0AAAAAA, self.inputs[1], self.clocks[0])
            shifter.setValue(0x0AAAAAA, self.inputs[2], self.clocks[0])
            shifter.setValue(0x0AAAAAA, self.inputs[3], self.clocks[0])
            shifter.setValue(0x0AAAAAA, self.inputs[4], self.clocks[1])
            shifter.setValue(0x0AAAAAA, self.inputs[5], self.clocks[1])
            shifter.setValue(0x0AAAAAA, self.inputs[6], self.clocks[1])
            shifter.setValue(0x0AAAAAA, self.inputs[7], self.clocks[1])
            shifter.setValue(0x0AAAAAA, self.inputs[8], self.clocks[2])
            shifter.setValue(0x0AAAAAA, self.inputs[9], self.clocks[2])
            shifter.setValue(0x0AAAAAA, self.inputs[10], self.clocks[2])
            shifter.setValue(0x0AAAAAA, self.inputs[11], self.clocks[2])
            sleep(0.5)
            shifter.clear()
            shifter.setValue(0x0555555, self.inputs[0], self.clocks[0])
            shifter.setValue(0x0555555, self.inputs[1], self.clocks[0])
            shifter.setValue(0x0555555, self.inputs[2], self.clocks[0])
            shifter.setValue(0x0555555, self.inputs[3], self.clocks[0])
            shifter.setValue(0x0555555, self.inputs[4], self.clocks[1])
            shifter.setValue(0x0555555, self.inputs[5], self.clocks[1])
            shifter.setValue(0x0555555, self.inputs[6], self.clocks[1])
            shifter.setValue(0x0555555, self.inputs[7], self.clocks[1])
            shifter.setValue(0x0555555, self.inputs[8], self.clocks[2])
            shifter.setValue(0x0555555, self.inputs[9], self.clocks[2])
            shifter.setValue(0x0555555, self.inputs[10], self.clocks[2])
            shifter.setValue(0x0555555, self.inputs[11], self.clocks[2])
            sleep(0.5)
        except KeyboardInterrupt:
            gpio.cleanup()
            running = False


if __name__ == "__main__":
    main()
