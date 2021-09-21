def main():

	num = int(input("Digite um número inteiro: "))
	size = len(str(num))
	sum = 0

	while size > 0:
		sum = sum + num % 10
		num = num // 10
		size = size - 1

	print(sum)

main()
