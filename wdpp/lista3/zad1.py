def pierwsza(n):
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True

def szczesliwa(n):
    if '777' in str(n):
        return True
    else:
        return False

ilosc_liczb = 0
for i in range(1, 100001):
    if pierwsza(i) and szczesliwa(i):
        print(i)
        ilosc_liczb += 1

print('\nLiczb szczesliwych i pierwszych od 1 do 100000 jest ' + str(ilosc_liczb))
