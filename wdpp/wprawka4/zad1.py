def crop(c, tab):
    return [c[1] if j > c[1] else j for j in [c[0] if i < c[0] else i for i in tab]]

print(crop([1,4],[3,4,5,100,2,-200]))
print(crop([0, 9.2], [-1.3, 2, 512, -2.4, 23.2, 5.6]))
