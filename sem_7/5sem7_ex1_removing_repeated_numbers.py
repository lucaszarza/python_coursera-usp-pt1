def remove_repetidos(lista):
	unique_list = []
	for i in lista:
		if i not in unique_list:
			unique_list.append(i)
	
	unique_list.sort()
	return unique_list

def test_ordered_list1():
	test1 = [10,4,6,1,3,67,82,2,1,3,9]
	assert remove_repetidos(test1) == [1, 2, 3, 4, 6, 9, 10, 67, 82]

def test_ordered_list2():
	test2 = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 10 ,9]
	assert remove_repetidos(test2) == [1, 2, 3, 4, 6, 7, 8, 9, 10]

def test_ordered_list3():
	test3 = [1, 2, 3, 3, 3, 4]
	assert remove_repetidos(test3) == [1, 2, 3, 4]


