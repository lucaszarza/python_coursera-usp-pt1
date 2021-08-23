# escreva o seu programa
def main():
    num = int(input("Digíte um inteiro: "))
    soma = 0
    
    while num != 0:
        soma = soma + num
        num = int(input("Digite um inteiro: "))
        
    print("A soma eh", soma)
    
main()