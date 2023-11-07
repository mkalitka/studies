import math

def machine_zero():
    ep = 1.0
    while 1 + ep != 1:
        ep /= 2
    return ep

zero = machine_zero()

maxIter = 10 ** 6

def test(x0, m, c):
    y = m if c % 2 == 0 else 2 * m
    c = int(math.floor(c / 2))

    def f(x):
        return (x ** 2) - y
    
    def newton(x0):
        r = x0
        i = 0
        while abs(f(r)) >= zero and i < maxIter:
            r = (r / 2) + y / (2 * r)
            i += 1
        return (r * (2 ** c), i)

    return newton(x0)

print(test(100, 0.5, 3))
