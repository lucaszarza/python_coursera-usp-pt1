
def main():
	n = 1
	list = []

	while n != 0:
		n = int(input("Digite um número: "))
		list.append(n)
		
	del(list[-1])
	list.reverse()
	for i in list: print(i)

main()