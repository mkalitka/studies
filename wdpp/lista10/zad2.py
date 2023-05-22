polskie_znaki = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
def ceasar(s, k):
    polskie_znaki = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    wynik = [polskie_znaki[(polskie_znaki.index(c) + k) % len(polskie_znaki)] for c in s]
    w = ""
    for i in wynik:
        w += i
    return w

with open("pop.txt") as f:
    slowa = f.readlines()

maks_dlugosc = 0
for i in slowa:
    if len(i) - 1 > maks_dlugosc:
        maks_dlugosc = len(i) - 1

for x in range(maks_dlugosc, 10, -1):
    pot = []
    for i in slowa:
        if len(i) - 1 == x:
            pot.append(i[:-1])
    for p in pot:
        for l in range(1, 32):
            o = ceasar(p, l)
            if o in pot:
                print(o, p)
                raise Exception
