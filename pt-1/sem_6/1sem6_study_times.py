def main():
	line = 1
	column = 1
	while line <= 10:
		while column <= 10:
			print(f'{line} x {column} = ', (line * column))
			colunm += 1
		print("-------------")
		column = 1
		line += 1

main()
