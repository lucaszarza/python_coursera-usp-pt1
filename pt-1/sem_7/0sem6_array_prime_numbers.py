def isPrime(x):
	factor = 2

	if x == 2: return True

	while x % factor != 0 and factor <= x/2:
		factor += 1

	if x % factor == 0:
		return False
	else:
		return True


def main():
	end = False	
	limit = int(input("Limite máximo: "))


	n = 2
	while n < limit:
		if isPrime(n):
			print(n, end=", ")
		n += 1

main()