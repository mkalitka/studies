def sortpts(c, list):
    return sorted([(((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2) ** (1 / 2), (a[0], a[1])) for a in list])

print(sortpts([2, 3], [[-6, 4], [0, 0], [2, -6], [3, 4]]))
