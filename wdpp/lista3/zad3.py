def usun_w_nawiasach(s):
    while s.find('(') != -1 and s.find(')') != -1 and s.find('(') < s.find(')'):
        start_index = s.find('(')
        end_index = s.find(')')
        s = s[:start_index] + s[end_index + 1:]
    return s

print(usun_w_nawiasach('raz dwa trzy raz (dwa) trzy raz dwa (trzy) asd (asdas)'))
print(usun_w_nawiasach('wladimir putin to jedna z (najglupszych) osob na swiecie'))
print(usun_w_nawiasach('(cenzura) hehe (cenzura) brak cenzury'))
