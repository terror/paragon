"""all statistics related logic"""


class Stats:
    """handles statistics compute and output"""

    def __init__(self, times):
        self.times = times

    @property
    def avg(self):
        """returns the average time"""
        return sum(self.times) / len(self.times)

    @property
    def range(self):
        """returns the range (min, max) of all times"""
        return (min(self.times), max(self.times))

    def standard_deviation(self):
        """calculates the standard deviation from the mean"""
        return round(
            (sum([((time - self.avg) ** 2) for time in self.times]) / len(self.times))
            ** 0.5,
            10,
        )

    def output(self):
        """prints stats to stdout"""
        print(
            "\nTime (mean \xB1 o): {:.2f} s \xB1 {:2f} s.".format(
                self.avg, self.standard_deviation()
            )
        )
        print(
            "Range (min ... max): {:.2f} s ... {:.2f} s.\n".format(
                self.range[0], self.range[1]
            )
        )
