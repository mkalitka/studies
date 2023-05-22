from losowanie_fragmentow import losuj_fragment

def losuj_haslo(n):
	haslo = ''
	while True:
		fragment = losuj_fragment()
		if len(fragment) + len(haslo) < n - 1:
			haslo += fragment
		elif len(fragment) + len(haslo) == n:
			haslo += fragment
			return haslo 

for i in range(10):
	print(losuj_haslo(8))

for i in range(10):
	print(losuj_haslo(12))
