def soma_elementos(lista):
	sum = 0
	for i in lista:
		sum += i

	return sum

def test_sum():
	test = [1, 2, 3, 4, 5]
	assert soma_elementos(test) == 15

def test_sum2():
	test = [5, 5, 4, 6, 9, 2, 5]
	assert soma_elementos(test) == 36