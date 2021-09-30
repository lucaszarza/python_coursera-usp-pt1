def factorial (n):
	if n < 0:
		return 0
	i = fat = 1
	while i <= n:
		fat = fat * i
		i = i + 1
	return fat

# def test_factorial0():
# 	assert factorial(0) == 1

# def test_factoria5():
# 	assert factorial(5) == 120

