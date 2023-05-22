def dist(o, list):
    return [((o[0] - i[0]) ** 2 + (o[1] - i[1]) ** 2) ** (1 / 2) for i in list]

print(dist([3, 4], [[2, 3], [-3, 6], [0, 0], [-1, 3]]))
