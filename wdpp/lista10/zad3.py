def lamiglowka(s, slownik = []):
    uzyte = []
    for znak, cyfra in slownik:
        s = s.replace(znak, cyfra)
        uzyte.append(znak)
        uzyte.append(cyfra)
    print(s)
    try:
        if eval(s) == True:
            return slownik
        else:
            return None
    except (SyntaxError, NameError):
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyzęóąśłżźćń' and c not in uzyte:
                for i in range(10):
                    if str(i) not in uzyte:
                        slo = slownik
                        slo.append((c, str(i)))
                        lamiglowka(s, slo)

print(lamiglowka("aaaa + bbbb == cccc"))
