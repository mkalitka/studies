def slownik(s):
    s = s.lower()
    powt_asc = [0] * 300
    for i in s:
        powt_asc[ord(i)] += 1
    return powt_asc

def czy_ukladalne(s1, s2):
    powt_s1 = slownik(s1.lower())
    powt_s2 = slownik(s2.lower())
    for i in range(300):
        if powt_s1[i] > powt_s2[i]:
            return False
    return True

print(czy_ukladalne("daniel starzynski", "lenaidsrtanskair takierqnyzi"))
print(czy_ukladalne("kotek", "lokomotywa"))
