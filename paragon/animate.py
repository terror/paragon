"""all animation related logic"""

from progress.bar import IncrementalBar
from progress.spinner import PixelSpinner


class Bar(IncrementalBar):
    """custom progress bar"""

    message = "Status"
    suffix = "%(percent).1f%% - ETA %(eta)ds"


class Animate:
    """handles progress bars and spinners"""

    def __init__(self, accuracy):
        self.bar = Bar(max=accuracy)
        self.spinner = PixelSpinner()

    def next(self):
        """advance the spinner and bar to the next iteration in cycle"""
        self.bar.next()
        self.spinner.next()

    def done(self):
        """complete the bar"""
        self.bar.finish()
