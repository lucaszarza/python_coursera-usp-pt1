def factorial(n):
    fat = 1
    while n > 0:
        fat = fat * n
        n = n - 1
    return fat

def main():
    num = 1
    print("Bem-vindo a sua calculadora de fatoriais em série! Para parar a execução digite um valor negativo")
    while num >=0:
        num = int(input("Digite o número que deseja o fatorial: "))
        result = factorial(num)
        print(f'O fatorial de {num} é {result}')
    print("***Fim do exercício de Fatorial***")


main()
