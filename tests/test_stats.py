"""all stats related tests"""

from paragon.stats import Stats


def test_mean():
    """test the mean calculation"""
    times = [
        ([1, 2, 3], 2),
        ([1, 5, 3, 20, 39, 10], 13),
        (
            [2, 420, 5.24, 6.22, 2, 90, 1.45, 2, 4, 5, 6, 1, 1, 3, 6, 7],
            35.119375000000005,
        ),
    ]
    for entry, ans in times:
        stats = Stats(entry)
        assert stats.avg == ans


def test_range():
    """test the range calculation"""
    ranges = [
        ([1, 2, 3], (1, 3)),
        ([1, 5, 3, 20, 39, 10], (1, 39)),
        ([2, 5000, 5.24, 6.22, 2, 90, 1.45, 2, 4, 5, 6, 1, 1, 3, 6, 7], (1, 5000)),
        (
            [
                2,
                5000,
                9,
                9222,
                0,
                1,
                5.24,
                6.22,
                2,
                90,
                1.45,
                2,
                4,
                5,
                6,
                1,
                1,
                3,
                6,
                7,
            ],
            (0, 9222),
        ),
    ]

    for entry, ans in ranges:
        stats = Stats(entry)
        assert stats.range == ans


def test_standard_deviation():
    """test the standard deviation calculation"""
    deviations = [
        ([1, 2, 3, 4, 5], 1.4142135624),
        ([10, 12, 23, 23, 16, 23, 21, 16], 4.8989794856),
        ([10, 12, 23, 23, 16, 23, 21, 16, 20, 300, 400, 500], 170.3287670621),
    ]

    for entry, ans in deviations:
        stats = Stats(entry)
        assert stats.standard_deviation() == ans
