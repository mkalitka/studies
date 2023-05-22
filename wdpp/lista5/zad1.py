def F(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def analiza_collatza(a, b):
    energie = []

    while a <= b:
        wynik = a
        energia = 0
        while wynik != 1:
            wynik = F(wynik)
            energia += 1
        energie.append(energia)
        a += 1

    energie = sorted(energie)
        
    srednia = 0
    for i in energie:
        srednia += i
    srednia /= len(energie)
    print(srednia)

    if len(energie) % 2 == 0:
        mediana = (energie[len(energie) // 2 - 1] + energie[len(energie) // 2]) / 2
    else:
        mediana = energie[len(energie) // 2]
    print(mediana)

    print(energie[0], energie[-1])

analiza_collatza(3, 11)
