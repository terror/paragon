"""all stats related tests"""

from paragon.stats import Stats


def test_mean():
    """test the mean calculation
    - stats.avg converts the mean to ms
    """
    times = [
        ([1, 2, 3], 2000),
        ([1, 5, 3, 20, 39, 10], 13000),
        ([2, 420, 5.24, 6.22, 2, 90, 1.45, 2, 4, 5, 6, 1, 1, 3, 6, 7], 35119.38),
    ]

    for entry, ans in times:
        stats = Stats(entry, "test")
        assert stats.avg == ans


def test_range():
    """test the range calculation
    - stats.range converts the ranges to ms
    """
    ranges = [
        ([1, 2, 3], (1000, 3000)),
        ([1, 5, 3, 20, 39, 10], (1000, 39000)),
        ([2, 5000, 5.24, 6.22, 2, 90, 1.45, 2, 4, 5, 6, 1, 1, 3, 6, 7], (1000, 5000000)),
        ([2, 5000, 9, 9222, 0, 1, 5.24, 6.22, 2, 90, 1.45, 2, 4, 5, 6, 1, 1, 3, 6, 7], (0, 9222000))
    ]

    for entry, ans in ranges:
        stats = Stats(entry, "test")
        assert stats.range == ans


def test_standard_deviation():
    """test the standard deviation calculation
    - stats.standard_deviation() converts each time to ms
    """
    deviations = [
        ([1, 2, 3, 4, 5], 1414.21),
        ([10, 12, 23, 23, 16, 23, 21, 16], 4898.98),
        ([10, 12, 23, 23, 16, 23, 21, 16, 20, 300, 400, 500], 170328.77),
    ]

    for entry, ans in deviations:
        stats = Stats(entry, "test")
        assert stats.standard_deviation() == ans
