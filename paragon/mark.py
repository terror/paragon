"""all time related logic"""

import time


class Mark:
    """mark subtraction, init, diff .. etc"""

    def __init__(self):
        self.time = time.perf_counter()

    def __sub__(self, other):
        """subtract two marks counts"""
        return round(other.time - self.time, 2)

    def diff(self):
        """diff's the current counter with init's counter"""
        return round(time.perf_counter() - self.time, 2)

    def reset(self):
        """reset the marks counter"""
        self.time = time.perf_counter()
