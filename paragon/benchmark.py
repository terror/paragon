"""all benchmark related logic"""
# pylint: disable = exec-used

import sys
import click
from paragon.stats import Stats
from paragon.utils import Utils
from paragon.mark import Mark
from paragon.animate import Animate


class Paragon:
    """handles code benchmarking"""

    @staticmethod
    def benchmark(name: str = None, accuracy: int = 1):
        """benchmark decorator
        - retrieves decoratored functions name and args
        - calls bench with the function call and scope

        :param name: name of benchmark
        :accuracy: number of iterations
        """

        def inner(func):
            def wrap(*args):
                nonlocal name

                start, func_name = Mark(), func.__name__

                try:
                    click.secho(
                        "Benchmark: {}".format(name or func_name),
                        fg="white",
                        bold=True,
                    )
                except AttributeError:
                    click.secho("Make sure you wrap your recursive functions!\n", err=True)
                    sys.exit(1)

                # gather locals and build code string
                env = {func_name: func}
                code = f"{func_name}(*{args})"

                # run bench
                Paragon.bench(code=code, env=env, accuracy=accuracy)

                print(f"✨ Done in {round(start.diff(), 2)} s ✨\n")

                return func(*args)
            return wrap
        return inner

    @staticmethod
    def bench(code: str, env: object = None, accuracy: int = 1):
        """benchmark function
        - benches passed in code, taking in optional locals and number
        of iterations

        :param code: code to benchmark
        :accuracy: number of iterations
        :env: locals
        """
        # don't need stdout
        Utils.redirect_stdout()

        # run once to make sure it's valid python
        err, status = Utils.run_once(code, env)
        if not status:
            raise err

        mark, animate, times = Mark(), Animate(accuracy), []
        for _ in range(accuracy):
            exec(code, globals(), env or globals())
            animate.next()
            times.append(mark.diff())
            mark.reset()

        # cleanup animation and output stats
        animate.done()
        Stats(times).output()
