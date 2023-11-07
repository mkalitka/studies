import timeit


def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def pierwsze_imperatywna(n):
    pierwsze = []
    for i in range(n):
        if czy_pierwsza(i):
            pierwsze.append(i)
    return pierwsze


def pierwsze_skladana(n):
    return [i for i in range(n) if czy_pierwsza(i)]


def pierwsze_funkcyjna(n):
    return list(filter(czy_pierwsza, range(n)))


def time_test():
    print("n\timperatywna\tskladana\tfunkcyjna\t")
    for n in range(10, 100, 10):
        print(f"{n}\t", end="")
        for f in [pierwsze_imperatywna, pierwsze_skladana, pierwsze_funkcyjna]:
            czas = timeit.timeit(lambda: f(n), number=20)
            print(f"{czas:.6f}\t", end="")
        print()


if __name__ == "__main__":
    time_test()
