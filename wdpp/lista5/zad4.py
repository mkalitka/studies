def usun_duplikaty(tab):
    tab = sorted(tab)
    ret = []
    for i in range(len(tab)):
        if tab[i] != tab[i - 1]:
            ret.append(tab[i])
    return ret

print(usun_duplikaty([1, 2, 5, 3, 2, 5, 2, 6, 7, 7]))
