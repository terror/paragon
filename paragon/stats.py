class Stats:
    def __init__(self, times):
        self.times = times

    @property
    def avg(self):
        return sum(self.times) / len(self.times)

    @property
    def range(self):
        return (min(self.times), max(self.times))

    def output(self):
        print("\n✨ Finished in {:.2f} seconds. ✨".format(sum(self.times)))
        print("✨ Average time: {:.2f} seconds. ✨".format(self.avg))
        print(
            "✨ Range: {:.2f} ... {:.2f} seconds. ✨\n".format(
                self.range[0], self.range[1]
            )
        )
