from datetime import datetime

class Tick:

    __on_tick = None
    __tick_count = 0
    __ms_per_tick = 250

    def elapsed_ms(self, last_time):
        dt = datetime.now() - last_time
        ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
        return ms

    def __init__(self, game):
        self.__on_tick = game.on_tick
        game.setTick(self)
        last_time = datetime.now()
        while True:
            if self.elapsed_ms(last_time) > self.__ms_per_tick:
                last_time = datetime.now()
                self.__tick_count = (self.__tick_count + 1) % 4
                self.__on_tick(self.__tick_count)

    def increase_velocity(self):
        if self.__ms_per_tick > 100:
            self.__ms_per_tick -= 10
