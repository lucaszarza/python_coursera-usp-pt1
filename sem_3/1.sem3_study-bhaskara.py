import math

print("** Bem-vindo à calculadora de Bhaskara! **")
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = (b ** 2) - (4 * a * c)

print(delta)
x1 = (- (b) + math.sqrt(delta)) / 2 * a
x2 = (- (b) - math.sqrt(delta)) / 2 * a

print(f'O valor de X1 é {x1}')
print(f'O valor de X2 é {x2}')
