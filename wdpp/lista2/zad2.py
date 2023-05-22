def koperta(n):
	n = 2 * n + 1
	for i in range(n):
		if i == 0 or i == n - 1:
			print('*' * n)
		elif i == n // 2:
			print('*' + ' ' * ((n - 3) // 2) + '*' + ' ' * ((n - 3) // 2) + '*')
		else:
			if i < n // 2:
				przerwy = i - 1
			else:
				przerwy = n - i - 2
			print('*' + ' '* przerwy + '*' + ' ' * (n - 2 * przerwy - 4) + '*' + ' ' * przerwy + '*')

koperta(4)
