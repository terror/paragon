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
