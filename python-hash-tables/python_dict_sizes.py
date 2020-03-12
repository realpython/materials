import sys
d = {}
last_size = 0
for i in range(1, 1000):
	d[i] = 0
	new_size = sys.getsizeof(d)
	if last_size != new_size:
		print(i, new_size)  # different for Python 2.7
		last_size = new_size
