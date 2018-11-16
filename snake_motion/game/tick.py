from datetime import datetime

class Tick:

    __on_tick = None
    __tick_count = 0
    __seconds_per_tick = 500

    def __init__(self, on_tick_callback):
        self.__onTick = on_tick_callback
        last_time = datetime.now()
        while True:
            if elapsed_ms(last_time) > self.__seconds_per_tick:
                last_time = datetime.now()
                self.__tick_count = (self.__tick_count + 1) % 4
                self.__on_tick(self.__tick_count)

    def elapsed_ms(last_time):
        dt = datetime.now() - last_time
        ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
        return ms

    def increase_velocity():
        if self.__seconds_per_tick > 100:
            self.__seconds_per_tick -= 5
