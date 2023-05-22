def podziel(s):
    tab = []
    f = 0
    for i in range(len(s)):
        if s[i] == " ":
            if s[f:i] != "":
                tab.append(s[f:i])
            f = i + 1
        if i == len(s) - 1:
            if s[f:i+1] != "":
                tab.append(s[f:i+1])
    return tab

print(podziel("ala ma    kota"))
