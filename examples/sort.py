import random


def main():
    for _ in range(500):
        a = [random.randint(1, 1000) for _ in range(100)]
        print(sort(a))


def sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a


main()
