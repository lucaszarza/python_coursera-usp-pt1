def main():

	print("****Primeiro exemplo - Frutas Exóticas com Array e For In****")
	frutas_exoticas = ["maça","jabuticaba","cupuaçu"]

	for fruta in frutas_exoticas:
		print(f'Eu adoro {fruta}')

	
	print("****Segundo exemplo - Counter com For In Range****")

	for i in range(10):
		print(f'counter {i}')

	print("****Terceiro exemplo - Counter com Range (2 args)****")

	for i in range (10,20):
		print(i)
	
	print("****Quarto exemplo - Range 3 args****")

	for i in range (0, 30, 3):
		print("tabuada do 3 - ", i)


	print("***Quinto exemplo - Variavel no range****")

	pares = range(0,50,2)

	for x in pares: print(x)


	print("****Sexto exemplo - Negativo****")

	numeros = range(10,0,-1)

	for y in numeros: print(y)

main()
