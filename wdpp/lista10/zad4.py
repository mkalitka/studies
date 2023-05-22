def sumy(tab):
    if len(tab) == 1:
        return set([tab[0]])
    sumy_bez_last = sumy(tab[:-1])
    dodane = set([x + tab[-1] for x in sumy_bez_last])
    return sumy_bez_last.union(dodane).union(set([tab[-1]])).union(set([0]))

print(sumy([1, 2, 3, 100]))
