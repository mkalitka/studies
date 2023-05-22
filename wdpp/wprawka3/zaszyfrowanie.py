with open('a.txt') as f:
	tekst = f.readlines()
	f.close()

deszyfr = ''
for i in tekst:
	deszyfr += i

kod = 'jaranie'
haslo = kod

while len(haslo) <= len(deszyfr):
	haslo += kod

while len(haslo) > len(deszyfr):
	haslo = haslo[:-1]

szyfr = ''
for i in range(len(haslo)):
	szyfr += str(ord(haslo[i]) ^ ord(deszyfr[i])) + ' '

with open('szyfr.txt', 'w') as f:
	f.write(szyfr)
	f.close()
