def szachownica(n, k):
	for i in range(2 * n):
		for l in range(k):
			for j in range(2 * n):
				if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
					print(' ' * 3, end='')
				else:
					print('#' * 3, end='')
			print()

szachownica(4, 3)
