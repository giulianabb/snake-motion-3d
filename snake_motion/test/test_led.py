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
        self.pause = 1

    def tick(self):
        gpio.output(self.clock, gpio.HIGH)
        sleep(self.pause)
        gpio.output(self.clock, gpio.LOW)
        sleep(self.pause)

    def setValue(self, value):
        for i in range(24):
            bitwise = 0x800000 >> i
            bit = bitwise & value
            if(1 == 0):
                gpio.output(self.inputB, gpio.LOW)
            else:
                gpio.output(self.inputB, gpio.HIGH)
            self.tick()

    def clear(self):
        gpio.output(self.clearPin, gpio.LOW)
        self.tick()
        gpio.output(self.clearPin, gpio.HIGH)

    def setupBoard(self):
        # gpio.setup(self.inputA, gpio.OUT)
        # gpio.output(self.inputA, gpio.HIGH)

        gpio.setup(self.inputB, gpio.OUT)
        gpio.output(self.inputB, gpio.LOW)

        gpio.setup(self.clock, gpio.OUT)
        gpio.output(self.clock, gpio.LOW)

        gpio.setup(self.clearPin, gpio.OUT)
        gpio.output(self.clearPin, gpio.HIGH)


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
            print("Realizando clear")
            shifter.clear()
            print("Setando valor")
            shifter.setValue(0x0AAAAAA)
            sleep(pause)
            shifter.clear()
            shifter.setValue(0x0555555)
            sleep(pause)
        except KeyboardInterrupt:
            gpio.cleanup()
            running = False


if __name__ == "__main__":
    main()
