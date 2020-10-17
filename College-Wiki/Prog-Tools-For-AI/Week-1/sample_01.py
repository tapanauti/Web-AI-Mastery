def spidermove(x, y):
    int x = Math.abs(x)
    int y = Math.abs(y)

    final = [][]
    for hor in range(0, x):
        for ver in range(0, y):
            final[hor][ver] = hor+ver


print(final)
