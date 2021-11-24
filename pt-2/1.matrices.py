A = [[1,2,3],
		 [4,5,6],
		 [7,8,9]]


def create_matrice(line_num, column_num):

	matrice = []
	for i in range(line_num):
		line = []
		for j in range(column_num):
			value = int(input(f'Digite o elemento [{i}][{j}] da matriz: '))
			line.append(value)
		matrice.append(line)

	return matrice

def main():
	

	line = int(input("Digite o número de linhas da matriz: "))
	column = int(input("Digite o número de colunas da matriz: "))

	print(create_matrice(line,column))

main()