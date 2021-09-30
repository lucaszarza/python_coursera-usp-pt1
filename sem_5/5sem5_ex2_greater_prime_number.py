def isPrime(k):
	prime = False

	if k <= 10:
		if k == 1:
			prime = False
		elif k == 2 or k == 3 or k == 5 or k == 7:
			prime = True
	else:
		if k % 2 == 0 or k % 3 == 0 or k % 5 == 0 or k % 7 == 0:
			prime = False
		else:
			prime = True

	return prime

def maior_primo(num):

	biggestPrimeNumber = 0 

	while (num > 0 and biggestPrimeNumber == 0):
		if isPrime(num):
			biggestPrimeNumber = num
		else:
			num = num - 1

	return biggestPrimeNumber


def test_biggest_prime_number():
	assert maior_primo(100) == 97
	assert maior_primo(10) == 7
	assert maior_primo(12) == 11	


def test_prime_numbers_true():
	assert isPrime(5) == True
	assert isPrime(11) == True
	assert isPrime(97) == True

def test_prime_numbers_false():
	assert isPrime(1) == False
	assert isPrime(10) == False
	assert isPrime(-3) == False		
