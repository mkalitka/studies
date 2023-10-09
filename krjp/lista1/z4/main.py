import random
import math


def main():
    n = int(input("Podaj liczbę losowań: "))
    accuracy = float(input("Podaj dokładność: "))
    ltwo = 0
    cltwt = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            ltwo += 1
        cltwt += 1
        pi = 4 * ltwo / cltwt
        if abs(pi - math.pi) < accuracy:
            break
    print("Przybliżenie liczby pi:", pi)
    print("Liczba losowań:", cltwt)


if __name__ == "__main__":
    main()

