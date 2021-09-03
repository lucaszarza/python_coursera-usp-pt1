def main():

    num1 = int(input("Digite o seu primeiro número: "))
    num2 = int(input("Digite o seu segundo número: "))
    num3 = int(input("Digite o seu terceiro número: "))

    if(num1 < num2 < num3):
        print("crescente")
    else:
        print("não está em ordem crescente")

main()
