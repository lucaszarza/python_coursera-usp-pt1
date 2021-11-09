def maior_elemento(lista):
	biggest = 0

	for i in lista:
		if i > biggest:
			biggest = i

	return biggest

def test_biggest_num():
	test = [1, 2, 3, 4, 5]
	assert maior_elemento(test) == 5


def test_biggest_num2():
	test = [5, 5, 4, 6, 9, 2, 5]
	assert maior_elemento(test) == 9


def test_biggest_num3():
	test1 = [10,4,6,1,3,67,82,2,1,3,9]
	assert maior_elemento(test1) == 82
