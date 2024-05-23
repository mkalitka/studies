# zrodlo: https://medium.com/quick-code/longest-common-increasing-subsequence-lcis-1d2fc2713cd6
# uwaga: ja zrobiłam pierdolnik z indeksami w tym lcis2 i lcis3
# ciekawostka: na stronie oprócz samego faktu, że w kodzie widać iterację od 1, trzykrotnie został wytłuszczony napis
#              "Note that this article is 1-indexed", który w niczym mi nie przeszkodził w popierdoleniu indeksów
#              i naprawianiu ich solidne 2h.
def printTable(t):
    for row in t:
        print(row)

# PODEJŚCIE PIERWSZE: O(n^3) <- zaraz to zoptymalizuję, ale najpierw jest łatwiej tak zrozumieć
# dp[i][j] = długość LCIS stworzonego z elementów a[0..i-1] i zakończonych b[j-1]
# wypełniamy tabelę wierszami; dla a[0..n-1] i b[0..m-1] mamy n+1 wierszy i m+1 kolumn
def lcis3(a, b):
    n = len(a) # a[0..i..n]
    m = len(b) # b[0..j..m]
    dp = [[0]*(m) for _ in range(n+1)]

    for i in range(1, n+1):     # i = [1..n]
        for j in range(0, m): # j = [1..m]
          # jeżeli aktualna wartość a[i-1] jest taka sama, jak b[j-1], to znaczy, że a[i-1] jest "dobrym" zakończeniem aktualnego podciągu
          # bo przypominam, że chcemy mieć podciąg kończący się na b[j-1]
            if (a[i-1] == b[j]):
                # oznaczamy, że "jakby co" znaleźliśmy już podciąg jednoelementowy
                dp[i][j] = 1
                # przechodzimy po wartościach podciągu b[0..j-1] i sprawdzamy końce dotychczas znalezionych podciągów
                for k in range(0, j):
                    # zauważmy, że jeżeli znaleźliśmy wcześniej podciąg rosnący kończący się liczbą mniejszą, niż aktualna wartość b[j-1]
                    # to na jego koniec możemy dodać b[j-1] i podciąg nadal będzie rosnący i będzie miał długość większą o 1
                    if (b[k] < a[i-1]):
                        dp[i][j] = max(dp[i][j], dp[i-1][k] + 1)
            # jeżeli a[i-1] nie jest równe b[j-1], to a[i-1] nie może kończyć podciągu, który ma się kończyć na b[j-1] (wow XD)
            else:
                # przepisujemy wartość z poprzedniego wiersza
                dp[i][j] = dp[i - 1][j]

        # ---------- wypisywanie ----------
        # print(f"a[{i-1}]: {a[i-1]}")
        # print(f"a[0..{i-1}]: {a[:i]}")
        # printTable(dp)

    printTable(dp)
    return max(dp[n])


# PODEJŚCIE DRUGIE: O(n^2)
# zauważmy, że w poprzednim podejściu wewnętrzna pętla po k nam pierdoliła złożoność
# tymczasem to, co nas interesuje, to największa znaleziona wartość z poprzedniego wiersza na indeksach[0..j-1] dla liczby mniejszej od a[i-1]
# wykonujmy więc z każdym obrocie mniejszej pętli 1 krok algorytmu szukania maksimum z poprzedniego wiersza
# dzięki temu będziemy mieć ciągle aktualną wartość
def lcis2(a, b):
    n = len(a) # a[0..i..n]
    m = len(b) # b[0..j..m]
    dp = [[0]*m for _ in range(n+1)] 

    for i in range(1, n+1):     # i = [1..n]
        lenmax = 0              # największa długość podciągu kończącego się liczbą mniejszą od a[i-1] dotychczas znalezionego w poprzednim wierszu
        for j in range(0, m): # j = [1..m]
            # kopiujemy wartość z poprzedniego wiersza (ona może się później zmienić na większą)
            dp[i][j] = dp[i-1][j]
            # jeżeli liczby są takie same, to postępujemy jak wcześniej w sumie
            if a[i-1] == b[j]:
                if dp[i][j] < lenmax + 1:
                    dp[i][j] = lenmax + 1
            # jeżeli spotkaliśmy mniejszą liczbę od a[i-1], być może musimy zaktualizować lenmax 
            # intuicja: dodać a[i-1] na koniec ciągu, którego długość jest przechowywana w dp[i-1][j]
            elif b[j] < a[i-1]:
                if dp[i-1][j] > lenmax:
                    lenmax = dp[i-1][j]   

        # ---------- wypisywanie ----------
        # print(f"a[{i-1}]: {a[i-1]}")
        # print(f"a[0..{i-1}]: {a[:i]}")
        # printTable(dp)   

    printTable(dp)
    return max(dp[n])


# Wersja O(n^2) z odyskiwaniem
def lcis_better(a, b):
    n = len(a)
    m = len(b)
    a = [float('inf')] + a # indeksujemy tablice od 1
    b = [float('inf')] + b
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # tablica do wyliczania wyniku 

    for i in range(1, n + 1):   # Iterujemy po prefiksach A
        lenmax = 0              # Zmienna przechowująca długość najdłuższego dotychczasowego podciągu z poprzedniego wiersza (indeksy od 0 do j) 
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j]     # domyślna wartość to przepisanie wartości z poprzedniego wiersza
            if a[i] == b[j]:            # Jeżeli ostatni element a == elemenentowi z b (czyli możemy dokleić b na koniec)
                if dp[i][j] < lenmax + 1:   # sprawdzamy czy opłaca nam się wybrać ten LCIS
                    dp[i][j] = lenmax + 1   # jeżeli tak zapamiętujemy wybór
            if b[j] < a[i]:                 # wyszukiwanie dotychczasowego maksymalnego LCIS (to co robiła wewnętrzna pętla) *
                if dp[i - 1][j] > lenmax:   # jeżeli któraś z wartości jest większa 
                    lenmax = dp[i - 1][j]   # aktualizujemy wartość lenmax

    # * tutaj kluczowe jest zauważenie, że szukamy tych wartości tylko do indeksu j w celu zachowania kolejności elementów
    # w wynikowym LCIS
    path = []                   # stos do odtwarzania listy od tyłu
    cur_len = max(dp[n])
    j = dp[n].index(cur_len) 
    prev_val = float('inf')
    while cur_len > 0:
        if dp[n][j] == cur_len and b[j] < prev_val:
            path.append(b[j])
            prev_val = b[j]
            cur_len -= 1
        j -= 1

    return max(dp[n]), path[::-1]

print(lcis_better([1, 2, 7, 10, 4, 5, 6, 9], [2, 7, 8, 4, 10, 3, 5, 6])) 
print(lcis_better([1, 7, 2], [2, 1, 4, 3, 7, 8])) 
print(lcis_better([2, 3, 1, 6, 5, 4, 6], [1, 3, 5, 6])) 
print(lcis_better([1, 2, 0, 2, 1], [1, 0, 1])) 
print(lcis_better([2, 5, 4, 10, 3, 6], [2, 5, 10, 6])) 