## <p align='center'>paragon</p>

<p align='center'>
  A tiny command line benchmarking utility (and a python library!)<br/><br/>
  <img src="https://github.com/terror/paragon/actions/workflows/ci.yml/badge.svg"/>
</p>

## Demo

[![asciicast](https://asciinema.org/a/fC4GTTlbRlTSUqAn7qQN20fTE.svg)](https://asciinema.org/a/fC4GTTlbRlTSUqAn7qQN20fTE)

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

@Paragon.benchmark(name="FizzBuzz!", accuracy=20)
def fizzbuzz(n):
    return list(
        map(
            lambda i: "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i),
            range(1, n),
        )
    )

if __name__ == "__main__":
    main()
```
