def silnia(n):
	return 1 if n == 1 else silnia(n - 1) * n

def ilosc_cyfr(n):
	dlugosc = len(str(n))
	if dlugosc == 1:
		tekst = ' cyfre'
	elif dlugosc > 1 and dlugosc < 5:
		tekst = ' cyfry'
	else:
		tekst = ' cyfr'
	return str(dlugosc) + tekst



for i in range(1, 101):
	print(str(i) + '! ma ' + ilosc_cyfr(silnia(i)))
