def main():
	n = int(input("Digite o número que deseja ter o fatorial: \n"))
	fat = 1
	counter = n
	i = 1

	while counter > 0:
		fat = counter * (counter - i)
		i = i + 1
		counter = counter - 1


main()