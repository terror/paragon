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
        err, status = Utils.run_once(code)
        if not status:
            raise err

        mark, animate, times = Mark(), Animate(accuracy), []
        for _ in range(accuracy):
            exec(code, globals(), globals())
            animate.next()
            times.append(mark.diff())
            mark.reset()

        # cleanup animation and output stats
        animate.done()
        Stats(times).output()
