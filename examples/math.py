a = 2
b = 12
for i in range(20000):
    x = a * b + i
    z = []
    for j in range(100):
        z.append(x + j * a)
    print(sum(z))
