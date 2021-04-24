"""all benchmark related logic"""
# pylint: disable = exec-used

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
            exec(code, globals(), globals())
        except (NameError, SyntaxError) as error:
            Utils.reset_stdout()
            raise error

        mark, animate, times = Mark(), Animate(accuracy), []
        for _ in range(accuracy):
            exec(code, globals(), globals())
            animate.next()
            times.append(mark.diff())
            mark.reset()

        animate.done()
        Utils.reset_stdout()

        stats = Stats(times)
        stats.output()
