"""all utility related logic"""
# pylint: disable = exec-used

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
    def get_filename_ext(path: str):
        """returns the name and extension of the last part in the path"""
        parts, ext = os.path.splitext(path)
        return (parts.split("/")[-1], ext)

    @staticmethod
    def verify_file(path):
        """verifies a python file to benchmark"""
        if not os.path.exists(path):
            return ("File does not exist.", "", False)

        name, ext = Utils.get_filename_ext(path)
        if ext != ".py":
            return ("File must be a python file.", False)

        return (open(path, "r").read(), name, True)

    @staticmethod
    def run_once(code, env: object = None):
        """run code once to make sure it's valid"""
        try:
            exec(code, globals(), env or globals())
            return (None, True)
        except (NameError, SyntaxError) as error:
            Utils.reset_stdout()
            return (error, False)
