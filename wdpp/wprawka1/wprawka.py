def invert(f, a, b, y, n=10):
	mid = (a + b) / 2
	print('obecnie:', mid, 'szukane:', y ** (1 / 2), 'roznica:', abs(mid - y ** (1 / 2)))
	if n > 0:
		if f(mid) < y:
			return invert(f, (a + b) / 2, b, y, n - 1)
		elif f(mid) == y:
			return mid
		else:
			return invert(f, a, (a + b) / 2, y, n - 1)
	else:
		return mid
		
print(invert(lambda x: x * x, 0, 100, 100, 20))
