def main():
    produto=1
    i = 0
    
    tamanho = int(input("Digite o tamanho da sequência de números: "))
    
    while i < tamanho:
        valor = int(input("Digite um valor a ser multiplicado: "))
        produto = produto * valor
        i+=1

    print("O produto dos valores é: ", produto)

main()
