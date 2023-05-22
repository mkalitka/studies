def kolko(n):
	if n % 2 == 0:
		n += 1
	radius = n // 2 
	for i in range(n):
		for j in range(n):
			x = i - radius
			y = j - radius
			if x * x + y * y <= radius ** 2 + 1:
				print('*', end='')
			else:
				print(' ', end='')
		print()


def balwan(maxx):
	for m in range(3):
		n = (m+1)* maxx // 3
		if n % 2 == 0:
			n -= 1
		radius = n // 2
		for i in range(n):
			print(' ' * ((maxx - n) // 2), end='')
			for j in range(n):
				x = i - radius
				y = j - radius
				if x * x + y * y <= radius ** 2 + 1:
					print('*', end='')
				else:
					print(' ', end='')
			print()

balwan(20)
