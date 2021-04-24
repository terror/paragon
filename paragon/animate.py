from progress.bar import IncrementalBar
from progress.spinner import PixelSpinner


class Bar(IncrementalBar):
    message = "Status"
    suffix = "%(percent).1f%% - ETA %(eta)ds"


class Animate:
    def __init__(self, accuracy):
        self.bar = Bar(max=accuracy)
        self.spinner = PixelSpinner()

    def next(self):
        self.bar.next()
        self.spinner.next()

    def done(self):
        self.bar.finish()
