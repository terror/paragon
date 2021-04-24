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

    def output(self):
        """prints stats to stdout"""
        print("\n✨ Finished in {:.2f} seconds. ✨".format(sum(self.times)))
        print("✨ Average time: {:.2f} seconds. ✨".format(self.avg))
        print(
            "✨ Range: {:.2f} ... {:.2f} seconds. ✨\n".format(
                self.range[0], self.range[1]
            )
        )
