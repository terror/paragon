import time


class Mark:
    def __init__(self):
        self.time = time.perf_counter()

    def diff(self):
        return time.perf_counter() - self.time

    def __sub__(self, o):
        return o.time - self.time
