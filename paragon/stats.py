class Stats:
    def __init__(self, times):
        self.times = times

    @property
    def avg(self):
        return sum(self.times) / len(self.times)

    @property
    def range(self):
        return (min(self.times), max(self.times))
