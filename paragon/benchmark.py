"""all benchmark related logic"""

from paragon.stats import Stats
from paragon.utils import Utils
from paragon.mark import Mark
from paragon.animate import Animate


class Paragon:
    """handles code benchmarking"""
    @staticmethod
    def bench(code: str, accuracy: int):
        """benchmark function

        :param code: code to benchmark
        :accuracy: number of iterations
        """
        # don't need stdout
        Utils.redirect_stdout()

        # run once to make sure it's valid python
        try:
            exec(code)
        except Exception as e:
            raise e

        start = Mark()
        times, prev = [], None
        animate = Animate(accuracy)

        for _ in range(accuracy):
            exec(code)
            animate.next()
            times.append(prev.diff() if prev is not None else start.diff())
            prev = Mark()

        animate.done()
        Utils.reset_stdout()
        stats = Stats(times)
        stats.output()
