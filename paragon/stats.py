"""all statistics related logic"""
import click
from paragon.utils import Utils


class Stats:
    """handles statistics compute and output"""

    def __init__(self, times, name):
        self.times = times
        self.name = name

    @property
    def avg(self):
        """returns the average time"""
        return round((sum(self.times) / len(self.times)) * 1000, 2)

    @property
    def range(self):
        """returns the range (min, max) of all times"""
        return (round(min(self.times) * 1000, 2), round(max(self.times) * 1000, 2))

    def standard_deviation(self):
        """calculates the standard deviation from the mean"""
        return round(
            (
                sum([(((time * 1000) - self.avg) ** 2) for time in self.times])
                / len(self.times)
            )
            ** 0.5,
            2,
        )

    def output(self):
        """prints stats to stdout"""
        Utils.reset_stdout()

        print(
            "\nTime ({} \xB1 {}): {} ms \xB1 {} ms.".format(
                click.style("mean", fg="green"),
                click.style("\u03C3", fg="green"),
                click.style("{}".format(self.avg), fg="green"),
                click.style("{}".format(self.standard_deviation()), fg="green"),
            )
        )

        print(
            "Range ({} ... {}): {} ms ... {} ms.\n".format(
                click.style("min", fg="blue"),
                click.style("max", fg="red"),
                click.style("{:.2f}".format(self.range[0]), fg="blue"),
                click.style("{:.2f}".format(self.range[1]), fg="red"),
            )
        )

        return {"average": self.avg, "range": self.range, "name": self.name}
