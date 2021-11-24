def main():
	num = int(input("Digite o número que deseja ter o fatorial: \n"))
	fat = 1
	n = num
	
	while num > 0:
		fat = fat * num
		num-=1

	print(f'O fatorial de {n} é {fat}') 


main()
