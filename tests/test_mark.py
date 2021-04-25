"""all mark related tests"""

import time
from paragon.mark import Mark


def test_subtract():
    """test mark subtraction"""
    start = Mark()
    time.sleep(2)
    end = Mark()
    assert round(end - start) == 2


def test_diff():
    """test mark diff"""
    start = Mark()
    time.sleep(2)
    assert round(start.diff()) == 2


def test_reset():
    """test mark reset"""
    start = Mark()
    time.sleep(3)
    start.reset()
    time.sleep(3)
    assert round(start.diff()) == 3
