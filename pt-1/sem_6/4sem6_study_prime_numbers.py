def main():
    n = int(input("Digite um número inteiro: "))

    while n > 0:
        if isPrime(n):
            print(n, "é primo")
        else:
            print(n, "não é primo")
        n = int(input("Digite um número inteiro: "))


def isPrime(num):
    factor = 2

    if (num == 2):
        return True

    while num % factor != 0 and factor < num / 2:
        factor = factor + 1

    if num % factor == 0:
        return False
    else:
        return True


main()
