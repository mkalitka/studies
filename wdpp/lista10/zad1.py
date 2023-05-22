def ceasar(s, k):
    polskie_znaki = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    wynik = [polskie_znaki[(polskie_znaki.index(c) + k) % len(polskie_znaki)] for c in s]
    w = ""
    for i in wynik:
        w += i
    return w

print(ceasar("wysokobłagorodje", 8))
print(ceasar("dziesięciominutowych", 12))
