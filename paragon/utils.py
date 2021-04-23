import sys


class Utils:
    @staticmethod
    def reset_stdout():
        sys.stdout = sys.__stdout__

    @staticmethod
    def redirect_stdout(r=None):
        sys.stdout = r
