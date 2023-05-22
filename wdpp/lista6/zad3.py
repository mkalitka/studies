def pierwsza(n):
    for i in range(2, int(n ** (1/2) + 1)):
        if n % i == 0:
            return False
    return True

def dzielniki(n):
    dz = []
    for i in range(2, n // 2 + 1):
        if n % i == 0 and pierwsza(i) == True:
            dz.append(i)
    return dz

print(dzielniki(123))
