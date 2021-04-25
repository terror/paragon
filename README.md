## <p align='center'>paragon</p>

<p align='center'>
  A tiny command line benchmarking utility (and a python library!)<br/><br/>
  <img src="https://github.com/terror/paragon/actions/workflows/ci.yml/badge.svg"/>
</p>

## Demo

[![asciicast](https://asciinema.org/a/zlYbpkGncIkB01vqU1BnEh5T0.svg)](https://asciinema.org/a/zlYbpkGncIkB01vqU1BnEh5T0)

## Features
- Statistical analysis
- Cool progress bars
- Python library
- Export results to various file formats (todo)

## Installation

You can install the command line utility via pip:

```bash
$ pip install paragon
```

## Usage
You can use paragon as a command line utility or a python library.

### CLI

After running --help:

```
Options:
  -a, --accuracy INTEGER  Number of iterations
  -f, --files PATH        Input file path(s)
  -o, --output PATH       Output file path
  --help                  Show this message and exit.
```

**Examples**:

Benchmarking code as a string:
```bash
$ paragon "print('hello, world')" -a 20
```

Providing a python file:
```bash
$ paragon -f /path/to/file.py
```

### Exporting results

You can use the -o option to specify an ouput file which will receive the results. Paragon currently supports
Markdown, CSV and JSON file formats.

For instance, specifying a Markdown output file will yield this result:

| Program | Average [s] | Min [s] | Max [s] |
|---|---|---|---|
| `for i in range(2500): print(i ** i)` | 102.45 | 97.6 | 114.0 |
| `comp` | 230.27 | 226.6 | 236.6 |
| `hello` | 10.23 | 10.1 | 10.5 |
| `sort` | 429.49 | 421.8 | 438.2 |

### Library

Example:

```python
from paragon import Paragon

n = 1000000

def main():
    """entry point"""
    fizzbuzz(n)
    fib_wrapper(30)

@Paragon.benchmark(name="FizzBuzz!", accuracy=20)
def fizzbuzz(n):
    return list(
        map(
            lambda i: "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i),
            range(1, n),
        )
    )

# You must wrap your recursive functions
@Paragon.benchmark(name="Fibonacci!", accuracy=20)
def fib_wrapper(n):
    def fib(n):
        return 1 if n in [0, 1] else fib(n - 1) + fib(n - 2)
    fib(n)

if __name__ == "__main__":
    main()
```

## Further Ramblings

Paragon is heavily inspired by the shell benchmarking tool [hyperfine](https://github.com/sharkdp/hyperfine). Although currently less mature, it has room to grow. For now, it is a simple tool that can be used to run quick and easy benchmarks for Python code with minimal setup.
