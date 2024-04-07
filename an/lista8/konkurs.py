import data
import matplotlib.pyplot as plt

h = lambda k, xs: xs[k] - xs[k - 1]

def m(xs, ys):
    def lamb(k, xs):
        if k == 0:
            return 0
        return h(k, xs) / (h(k, xs) + h(k + 1, xs))

    def d(k, xs, ys):
        def iloraz_roznicowy(xs, ys):
            if len(xs) == 1:
                return ys[0]
            return (iloraz_roznicowy(xs[1:], ys[1:]) - iloraz_roznicowy(xs[:-1], ys[:-1])) / (xs[-1] - xs[0])

        if k == 0:
            return 0
        return 6 * iloraz_roznicowy(xs[(k - 1):(k + 2)], ys[(k - 1):(k + 2)])

    nl = len(xs) - 1
    q = [0 for _ in range(nl)]
    u = [0 for _ in range(nl)]
    l = [lamb(k, xs) for k in range(nl)]
    df = [d(k, xs, ys) for k in range(nl)]
    for i in range(1, nl):
        p = l[i] * q[i - 1] + 2
        q[i] = (l[i] - 1) / p
        u[i] = (df[i] - l[i] * u[i - 1]) / p
    mo = [0 for _ in range(nl + 1)]
    mo[nl - 1] = u[nl - 1]

    for i in range(nl - 2, 0, -1):
        mo[i] = u[i] + q[i] * mo[i + 1]

    return mo

def s(xs, ys, ms, k):
    return lambda x: ((ms[k - 1] * (xs[k] - x) ** 3) / 6 + (ms[k] * (x - xs[k - 1]) ** 3) / 6 + \
        (ys[k - 1] - (ms[k - 1] * h(k, xs) ** 2) / 6) * (xs[k] - x) + \
        (ys[k] - (ms[k] * h(k, xs) ** 2) / 6) * (x - xs[k - 1])) / h(k, xs)

def fs(xs, ys):
    ms = m(xs, ys)
    def res(x):
        for i in range(1, len(xs)):
            if xs[i - 1] <= x < xs[i]:
                return s(xs, ys, ms, i)(x)
    return res 

sx1 = fs(data.ts1, data.xs1)
sy1 = fs(data.ts1, data.ys1)
plt.plot([sx1(u) for u in data.us1], [sy1(u) for u in data.us1])

sx2 = fs(data.ts2, data.xs2)
sy2 = fs(data.ts2, data.ys2)
plt.plot([sx2(u) for u in data.us2], [sy2(u) for u in data.us2])

sx3 = fs(data.ts3, data.xs3)
sy3 = fs(data.ts3, data.ys3)
plt.plot([sx3(u) for u in data.us3], [sy3(u) for u in data.us3])

sx4 = fs(data.ts4, data.xs4)
sy4 = fs(data.ts4, data.ys4)
plt.plot([sx4(u) for u in data.us4], [sy4(u) for u in data.us4])

sx5 = fs(data.ts5, data.xs5)
sy5 = fs(data.ts5, data.ys5)
plt.plot([sx5(u) for u in data.us5], [sy5(u) for u in data.us5])

sx6 = fs(data.ts6, data.xs6)
sy6 = fs(data.ts6, data.ys6)
plt.plot([sx6(u) for u in data.us6], [sy6(u) for u in data.us6])

sx7 = fs(data.ts7, data.xs7)
sy7 = fs(data.ts7, data.ys7)
plt.plot([sx7(u) for u in data.us7], [sy7(u) for u in data.us7])

sx8 = fs(data.ts8, data.xs8)
sy8 = fs(data.ts8, data.ys8)
plt.plot([sx8(u) for u in data.us8], [sy8(u) for u in data.us8])

sx9 = fs(data.ts9, data.xs9)
sy9 = fs(data.ts9, data.ys9)
plt.plot([sx9(u) for u in data.us9], [sy9(u) for u in data.us9])

sx10 = fs(data.ts10, data.xs10)
sy10 = fs(data.ts10, data.ys10)
plt.plot([sx10(u) for u in data.us10], [sy10(u) for u in data.us10])

sx11 = fs(data.ts11, data.xs11)
sy11 = fs(data.ts11, data.ys11)
plt.plot([sx11(u) for u in data.us11], [sy11(u) for u in data.us11])

sx12 = fs(data.ts12, data.xs12)
sy12 = fs(data.ts12, data.ys12)
plt.plot([sx12(u) for u in data.us12], [sy12(u) for u in data.us12])

sx13 = fs(data.ts13, data.xs13)
sy13 = fs(data.ts13, data.ys13)
plt.plot([sx13(u) for u in data.us13], [sy13(u) for u in data.us13])

sx14 = fs(data.ts14, data.xs14)
sy14 = fs(data.ts14, data.ys14)
plt.plot([sx14(u) for u in data.us14], [sy14(u) for u in data.us14])

sx15 = fs(data.ts15, data.xs15)
sy15 = fs(data.ts15, data.ys15)
plt.plot([sx15(u) for u in data.us15], [sy15(u) for u in data.us15])

plt.xlim(0.0, 180.0)
plt.ylim(-4, 20.0)
plt.show()
