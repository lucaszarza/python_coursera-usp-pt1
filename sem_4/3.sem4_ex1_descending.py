def main():

    descending = True
    previous_value = int(input("Digite o primeiro número da sequência: "))
    value = 1

    while descending and value != 0:
        value = int(input("Digite o próximo número da sequência: "))
        if value > previous_value:
            descending = False
        else:
            previous_value = value
        value-=1


    if descending:
        print("Parabéns, sua sequência está na ordem decrescente!")
    else:
        print("Poxa vida, sua sequência não está na ordem crescente!")
    
    
main()
