def main():
	arr = []
	n = 1
	while (n != 0):
		n = int(input("Digite um numero maior que zero: "))	
		arr.append(n)

	arr.reverse()
	print(arr)

main()
