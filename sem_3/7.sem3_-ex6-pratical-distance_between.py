import math

def main():

    x1 = int(input("Digite a coordenada X do primeiro ponto: "))
    y1 = int(input("Digite a coordenada Y do primeiro ponto: "))
    x2 = int(input("Digite a coordenada X do segundo ponto: "))
    y2 = int(input("Digite a coordenada Y do segundo ponto: "))

    
    result = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    if result >= 10:
        print("longe")
    else:
        print("perto")

main()
