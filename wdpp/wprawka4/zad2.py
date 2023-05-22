def in_rectangle(ld, pg, list):
    return [ld[0] <= c[0] and ld[1] <= c[1] and pg[0] >= c[0] and pg[1] >= c[1] for c in list]

print(in_rectangle([-5, -5], [5, 5], [[0, 2], [5, 3], [-2, 5], [-6, 3], [0, -5.5], [3, -4], [-5, 7]]))
