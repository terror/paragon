"""all utility related logic"""
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
