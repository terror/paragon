from paragon import Paragon

n = 1000000


def main():
    math(n)
    fizzbuzz(n)
    fib_wrapper(30)
    fib(30)


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


@Paragon.benchmark(name="Fibonacci!", accuracy=20)
def fib_wrapper(n):
    def fib(n):
        return 1 if n in [0, 1] else fib(n - 1) + fib(n - 2)

    fib(n)


@Paragon.benchmark(name="Fibonacci!", accuracy=20)
def fib(n):
    return 1 if n in [0, 1] else fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    main()
