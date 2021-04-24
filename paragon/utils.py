"""all utility related logic"""
import os
import sys


class Utils:
    """utility methods"""

    @staticmethod
    def reset_stdout():
        """set stdout back to normal"""
        sys.stdout = sys.__stdout__

    @staticmethod
    def redirect_stdout(redirect_value=None):
        """set stdout to provided value or None"""
        sys.stdout = redirect_value

    @staticmethod
    def verify_file(file):
        """verifies a python file to benchmark"""
        if not os.path.exists(file):
            return ("File does not exist.", False)

        _, ext = os.path.splitext(file)
        if ext != ".py":
            return ("File must be a python file.", False)

        return (open(file, "r").read(), True)
