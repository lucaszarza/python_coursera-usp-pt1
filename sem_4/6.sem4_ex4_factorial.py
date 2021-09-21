def main():

	num = int(input("Digite o número que deseja obter o fatorial: "))
	fat = 1

	if num == 0:
		print("1")

	while (num > 0):
		fat = fat * num
		num = num - 1	
	
	print(fat)

main()	
