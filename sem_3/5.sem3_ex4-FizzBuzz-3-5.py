def main():

    num = int(input("Digite o seu número: "))

    if(num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    else:
        print(num)

main()
