def factorial(num):	
	fat = 1	
	
	if (num == 0):
		return 1
	elif (num < 0):
		return error
	else:
		while (num > 0):
			fat = fat * num
			num = num - 1
		
		return fat

def binomial_coefficient(k, n):
	result = (factorial(k)//(factorial(n)*factorial(k-n)))
	
	return result


def main():
	print("Bem vindo à calculadora de coeficiente binomial!")
	n = int(input("Digite o valor de n: "))
	k = int(input("Digite o valor de k: "))

	print(binomial_coefficient(n, k))

main()

