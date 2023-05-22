with open('szyfr.txt', 'r') as f:
	tekst = f.read()
	f.close()

tekst = tekst.split()

kod = 'jaranie'
haslo = kod
while len(haslo) < len(tekst):
	haslo += kod
while len(haslo) > len(tekst):
	haslo = haslo[:-1]

deszyfr = ''
for i in range(len(tekst)):
	deszyfr += chr(int(tekst[i]) ^ ord(haslo[i]))

print(deszyfr)
