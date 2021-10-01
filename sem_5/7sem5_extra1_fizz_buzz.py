def fizzbuzz(num):
	if num % 3 == 0 and num % 5 != 0:
		return "Fizz"
	elif num % 3 != 0 and num % 5 == 0:
		return "Buzz"
	elif num % 3 == 0 and num % 5 == 0:
		return "FizzBuzz"
	else:
		return num

def test_fizz():
	assert fizzbuzz(3) == "Fizz"

def test_buzz():
	assert fizzbuzz(5) == "Buzz"

def test_fizzbuzz():
	assert fizzbuzz(15) == "FizzBuzz"

def test_num():
	assert fizzbuzz(4) == 4
