def main():

    adjacent = False
    value = int(input("Digite seu número, vamos verificar se ele possui adjacentes iguais: "))
    size = len(str(value))

    while not adjacent and size > 0:
        unit = value % 10
        decimal = (value // 10) % 10
        if (unit == decimal):
            adjacent = True
        else:
            value = value // 10
        size-=1


    if adjacent:
        print("sim")
    else:
        print("não")
    
main()
