def palindromy(a, b):
    liczby = [True] * b
    if a < 2:
        a = 2
    for i in range(a):
        liczby[i] = False
    for i in range(2, int(b ** (1/2) + 1)):
        for j in range(i * i, b, i):
            liczby[j] = False
    wynik = []
    x = 0
    for i in liczby:
        if i == True:
            if str(x) == str(x)[::-1]:
                wynik.append(x)
        x += 1
    return wynik

print(palindromy(120, 1203))
