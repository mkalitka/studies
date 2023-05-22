with open('popularne_slowa.txt') as f:
    dane = f.readlines()
    f.close()


for i in range(len(dane)):
    dane[i] = dane[i][:-1]

for i in dane:
    if i[::-1] and i != i[::-1] in dane:
        print(i, i[::-1])
        dane.remove(i)
        dane.remove(i[::-1])
