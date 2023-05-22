import random
from collections import defaultdict as dd

pol_ang = dd(lambda:[])

for x in open('pol_ang.txt'):
    x = x.strip()
    L = x.split('=')
    if len(L) != 2:
        continue    
    pol, ang = L
    pol_ang[pol].append(ang)

najcz = {}
for x in open('brown.txt'):
    x = x.strip()
    L = x.split()
    for i in L:
        try:
            najcz[i.lower()] += 1
        except Exception:
            najcz[i.lower()] = 1
    
def tlumacz(polskie):
    wynik = []
    for s in polskie:
        if s in pol_ang:
            maks = 0
            slowo = ''
            for i in pol_ang[s]:
                try:
                    if najcz[i] > maks:
                        maks = najcz[i.lower()]
                        slowo = i.lower()
                except Exception:
                    pass
            if slowo == '':
                slowo = random.choice(pol_ang[s])
            wynik.append(slowo)
        else:
            wynik.append('[?]')
    return ' '.join(wynik)
    
zdanie = 'chłopiec z dziewczyna pójść do kino'.split()

for i in range(15):
    print (tlumacz(zdanie))            
            
