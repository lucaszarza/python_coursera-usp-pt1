def main():

	num = int(input("Digite o número: "))
	size = len(str(num))
	adjacent = False
	
	if len(str(num)) == 1:
		adjacent = False
		print("não")
		return

	while size > 0 or len(str(num)) != 1:
		if (((num // 10) % 10) == num % 10):
			adjacent = True
		num = num // 10
		size = size -1		
	
	if adjacent:
		print("sim")
	else:
		print("não")

main()
	

		
