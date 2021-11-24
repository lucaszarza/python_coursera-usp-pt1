def vogal(var):
	vowels = ['A','E','I','O','U','a','e','i','o','u']

	for letter in vowels:
		if var in vowels:
			return True
		else:
			return False


def test_vowel_true():
	assert vogal('a') == True
	assert vogal('U') == True
	assert vogal('E') == True
	assert vogal('i') == True

def test_vowel_false():
	assert vogal('B') == False
	assert vogal('C') == False
	assert vogal(0) == False
	assert vogal('Z') == False
	assert vogal('D') == False
