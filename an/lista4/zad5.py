def machine_zero():
    ep = 0.1
    while 1 + ep != 1:
        ep /= 10
    return ep

zero = machine_zero()

maxIter = 10 ** 6

def test(x0, R):
    def f(x):
        return 1/x - R
    
    def newton(x0):
        res = x0
        i = 0
        while abs(f(res)) >= zero and i < maxIter:
            res = res * (2 - res * R)
            i += 1
        return (res, i)

    return newton(x0)

print(test(0.2, 2))
print(test(0.3, 4))
