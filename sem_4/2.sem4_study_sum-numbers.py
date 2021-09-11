def main():
    result = 0
    i = 0
    total = 0
    
    number = int(input("Digite o número que deseja somar: "))
    size = len(str(number))

    while size > i:
        result = number % 10
        total += result
        i+=1
    
    print("O resultado da soma dos valores é:", total)
   

main()
