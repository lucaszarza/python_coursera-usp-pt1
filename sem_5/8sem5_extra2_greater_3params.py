def maximo (n1, n2, n3):
	if n1 > n2 and n2 > n3:
		return n1
	elif n1 < n2 and n2 < n3:
		return n3
	else: 
		return n2


def test_n1():
	assert maximo(30, 14, 10) == 30
	assert maximo(5, 3, 2) == 5
	assert maximo(1, 0, -1) == 1

def test_n2():
	assert maximo(1, 2, 0) == 2
	assert maximo(5, 10, 3) == 10
	assert maximo(-5, 5, 3)	== 5

def test_n3():
	assert maximo(1, 5, 10) == 10
	assert maximo(-10, -3, -1) == -1
	assert maximo(10, 50, 100) == 100
