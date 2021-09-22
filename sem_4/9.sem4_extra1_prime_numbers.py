# -*- coding: utf-8 -*-
def main():
	num = int(input("Digíte seu número: "))
	
	if num % num == 0 and num % 1 == 0:
		if num == 1:
			print("não primo")
		elif num == 2 or num == 3 or num == 5 or num == 7:
			print("primo")
		else:
			if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
				print("não primo")
			else:
				print("primo")
main()
 
