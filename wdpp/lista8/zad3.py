def mozliwe(s):
    s = s.lower()
    perms = []
    if len(s) == 1:
        return s
    for c in s:
        for a in mozliwe(s.replace(c, "", 1)):
            perms.append(c + a) 
    return perms

print(mozliwe("Mikołaj"))
