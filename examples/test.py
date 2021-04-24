"""testing library functionality"""

from paragon import Paragon

n = 1000000


def main():
    """entry point"""
    math(n)
    fizzbuzz(n)


@Paragon.benchmark(name="FizzBuzz!", accuracy=20)
def fizzbuzz(n):
    return list(
        map(
            lambda i: "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i),
            range(1, n),
        )
    )


@Paragon.benchmark(name="Math", accuracy=20)
def math(n):
    ans = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    return ans


if __name__ == "__main__":
    main()
