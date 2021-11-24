def maximo(n1, n2):
	if (n1 > n2):
		return n1
	else:
		return n2

def test_scenario1():
	assert maximo(1,2) == 2

def test_scenario2():
	assert maximo(9,10) == 10

def test_scenario3():
	assert maximo(3,-3) == 3
