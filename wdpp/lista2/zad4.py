from duze_cyfry import daj_cyfre

def cyfra(n):
	cyfry = [int(d) for d in str(n)]
	for j in range(5):
		for i in cyfry:
			print(daj_cyfre(i)[j], end=' ')
		print()

cyfra(12938342)
