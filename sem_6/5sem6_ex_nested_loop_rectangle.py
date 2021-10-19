def main():
	w = int(input("Digite a largura: "))
	h = int(input("Digite a altura: "))
	i = 0
	j = 0

	while i < h:
		while j < w:
			print("#", end='')
			j += 1
		print()
		j = 0
		i += 1

main()
