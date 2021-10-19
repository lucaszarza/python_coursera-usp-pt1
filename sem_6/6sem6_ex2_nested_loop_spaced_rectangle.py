def main():
	width = int(input("Digite a largura: "))
	height = int(input("Digite a altura: "))
	i = 1
	j = 1

	while i <= height:
		while j <= width:
			if (j == 1 or j == width or i == 1 or i == height):
				print("#", end='')
			else:
				print(" ", end='')
			j += 1
		print()
		j = 1
		i += 1


main()
