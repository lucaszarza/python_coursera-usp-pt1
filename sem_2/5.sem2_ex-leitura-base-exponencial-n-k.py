# escreva o seu programa

def main():
    n = int(input("Digite o número base: "))
    k = int(input("Digite o número expoente: "))
    
    total = n ** k
    
    print(f'O número {n} elevado a {k} é {total}')
    
main()