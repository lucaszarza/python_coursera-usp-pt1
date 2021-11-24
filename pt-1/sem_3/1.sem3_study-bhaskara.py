import math

print("** Bem-vindo à calculadora de Bhaskara! **")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz1 = (- b + math.sqrt(delta)) / (2 * a)
    print(f'O valor único da raiz é {raiz1}')
else:
    raiz1 = (- b + math.sqrt(delta)) / (2 * a)
    raiz2 = (- b - math.sqrt(delta)) / (2 * a)
    print(f'O valor da primeira raiz é {raiz1}')
    print(f'O valor da segunda raiz é {raiz2}')
