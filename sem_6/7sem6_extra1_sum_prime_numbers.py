def n_primos(num):
	counter = 0
	while counter < (num / 2):
		if is_prime(num):
			counter = counter + 1
		else:
			num = num - 1
	return counter

def is_prime(num):
	factor = 2

	if (num == 2):
		return True

	while num % factor != 0 and factor < num / 2:
		factor = factor + 1

	if num % factor == 0:
		return False
	else:
		return True

def main():
	n = int(input("Digite um número: "))

	while (n != 0):
		print(n_primos(n))
		n = int(input("Digite um número: "))

main()
