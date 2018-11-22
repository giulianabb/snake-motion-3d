import RPi.GPIO as gpio
from time import sleep


class Shifter():
    """
        Classe para setar o valor de um shift register.
        Adaptado de:
            https://www.instructables.com/id/Using-a-shift-register-with-Raspberry-Pi/

        Vcc: GPIO pin 2
        Ground: GPIO pin 6
        Clock: GPIO 7
        NOT Clear: GPIO 11
        Input A: pin 13
        Input B: pin 15

    """
    # inputA = None  # default: 15
    inputB = None  # default: 26
    clock = None  # default: 23
    clearPin = None  # default: 24

    def __init__(self, inputA=15, inputB=26,
                 clock=23, clearPin=24):
        # self.inputA = inputA
        self.inputB = inputB
        self.clock = clock
        self.clearPin = clearPin
        self.setupBoard()
        self.pause = 500

    def tick(self):
        gpio.output(Shifter.clock, gpio.HIGH)
        sleep(self.pause)
        gpio.output(Shifter.clock, gpio.LOW)
        sleep(self.pause)

    def setValue(self, value):
        for i in range(24):
            bitwise = 0x800000 >> i
            bit = bitwise & value
            if(bit == 0):
                gpio.output(Shifter.inputB, gpio.LOW)
            else:
                gpio.output(Shifter.inputB, gpio.HIGH)
            Shifter.tick(self)

    def clear(self):
        gpio.output(Shifter.clearPin, gpio.LOW)
        Shifter.tick(self)
        gpio.output(Shifter.clearPin, gpio.HIGH)

    def setupBoard(self):
        # gpio.setup(Shifter.inputA, gpio.OUT)
        # gpio.output(Shifter.inputA, gpio.HIGH)

        gpio.setup(Shifter.inputB, gpio.OUT)
        gpio.output(Shifter.inputB, gpio.LOW)

        gpio.setup(Shifter.clock, gpio.OUT)
        gpio.output(Shifter.clock, gpio.LOW)

        gpio.setup(Shifter.clearPin, gpio.OUT)
        gpio.output(Shifter.clearPin, gpio.HIGH)


def main():
    pause = 0.5
    gpio.setmode(gpio.BOARD)
    shifter = Shifter()
    running = True
    while running:
        try:
            # shifter.clear()
            # shifter.setValue(1)
            # sleep(1)
            shifter.clear()
            shifter.setValue(0x0AAAAAA)
            sleep(pause)
            shifter.clear()
            shifter.setValue(0x0555555)
            sleep(pause)
        except KeyboardInterrupt:
            running = False


if __name__ == "__main__":
    main()
