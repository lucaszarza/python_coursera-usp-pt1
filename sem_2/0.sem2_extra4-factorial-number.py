def main():
        
        num = int(input("Digite o número que deseja ter o fatorial: \n"))
        initial_number = num
        fat = 1
                
        while num > 0:
                fat = fat * num
                num = num - 1

        print("O fatorial de %d é" %initial_number, fat)

main()
