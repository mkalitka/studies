import math

ep = 1e-8
maxIter = 10 ** 7

def f(x):
    return (x ** 4) - math.log(x + 4)

def bisection(a, b):
    # Jeśli znaki są takie same, to nie ma miejsca zerowego
    if f(a) * f(b) > 0:
        return False
    
    rev = f(a) >= 0
    m = 0.5 * (a + b)
    i = 0
    while abs(f(m)) >= ep and i < maxIter:
        if(rev):
            if f(m) > 0:  a = m
            else: b = m
        else:
            if f(m) < 0:  a = m
            else: b = m
        i += 1
        m = 0.5 * (a + b)
    return m

x0 = bisection(1.0, 2.0)
x1 = bisection(-1.5, -0.5)

print(x1)
print(f(x1))
