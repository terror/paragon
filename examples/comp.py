def random_computation():
    a, b = 2, 12
    for i in range(20000):
        x, z = a * b + i, []
        for j in range(100):
            z.append(x + j * a)
        print(sum(z))


random_computation()
