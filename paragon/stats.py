"""all statistics related logic"""
import click
from paragon.utils import Utils


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
        Utils.reset_stdout()

        print(
            "\nTime ({} \xB1 {}): {} s \xB1 {} s.".format(
                click.style("mean", fg="green"),
                click.style("\u03C3", fg="green"),
                click.style("{:.2f}".format(self.avg), fg="green"),
                click.style("{:.2f}".format(self.standard_deviation()), fg="green"),
            )
        )

        print(
            "Range ({} ... {}): {} s ... {} s.\n".format(
                click.style("min", fg="blue"),
                click.style("max", fg="red"),
                click.style("{:.2f}".format(self.range[0]), fg="blue"),
                click.style("{:.2f}".format(self.range[1]), fg="red"),
            )
        )
