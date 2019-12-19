import time

SECS_IN_DAY = 24 * 60 * 60
SECS_IN_HOUR = 60 * 60
SECS_IN_MIN = 60


class MagicTimer:

    def __init__(self, t_zero=None):
        if t_zero:
            self.t_zero = t_zero
        else:
            self.t_zero = time.time()

    def delta(self):
        "Return time elapsed in seconds"
        return time.time() - self.t_zero

    def time_elapsed(self):
        "Return time elapsed in days, hours, minutes, seconds, milliseconds"
        delta = self.delta()
        
        days = int(delta / SECS_IN_DAY)
        remainder = delta - days * SECS_IN_DAY

        hours = int(remainder / SECS_IN_HOUR)
        remainder -= hours * SECS_IN_HOUR

        minutes = int(remainder / SECS_IN_MIN)
        remainder -= minutes * SECS_IN_MIN

        seconds = int(remainder)
        remainder -= seconds

        milliseconds = int(remainder * 1000)
        # remainder -= milliseconds / 1000

        return days, hours, minutes, seconds, milliseconds

    def __str__(self):
        "Return time elapsed in format: days:hours:minutes:seconds:milliseconds"
        days, hours, minutes, seconds, milliseconds = self.time_elapsed()

        return "{}:{:02d}:{:02d}:{:02d}:{:03d}".format(days, hours, minutes, seconds, milliseconds)

    def __repr__(self):
        return "{}(t_zero={})".format(__class__.__name__, self.t_zero)
