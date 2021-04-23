import time
import sys
from progress.bar import IncrementalBar
from paragon.stats import Stats
from paragon.utils import Utils


class Bar(IncrementalBar):
    message = "Status"
    suffix = "%(percent).1f%% - ETA %(eta)ds"


class Benchmark:
    @staticmethod
    def bench(code, accuracy):
        # don't need stdout
        Utils.redirect_stdout()

        # run once to make sure it's valid python
        try:
            exec(code)
        except Exception as e:
            raise e

        start = time.perf_counter()
        times, prev = [], None
        with Bar(max=accuracy) as bar:
            for _ in range(accuracy):
                exec(code)
                bar.next()
                if prev is not None:
                    times.append(time.perf_counter() - prev)
                else:
                    times.append(time.perf_counter() - start)
                prev = time.perf_counter()

        bar.finish()
        Utils.reset_stdout()
        stats = Stats(times)

        print("✨ Finished in {:.2f} seconds. ✨".format(time.perf_counter() - start))
        print("✨ Average time: {:.2f} seconds. ✨".format(stats.avg))
        print(
            "✨ Range: {:.2f} ... {:.2f} seconds. ✨".format(stats.range[0], stats.range[1])
        )
        print()
