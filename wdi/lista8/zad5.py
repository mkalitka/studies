def minimum(tab):
    if len(tab) == 1:
        return tab[0]
    tab1 = tab[0:len(tab)//2]
    tab2 = tab[(len(tab)//2):len(tab)]
    min1 = minimum(tab1)
    min2 = minimum(tab2)
    if min1 < min2:
        return min1
    else:
        return min2

print(minimum([1, 5, 2, -1, 6, -2314, 8, -23, 123, -124]))
