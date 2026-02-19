def compostos():
    num = float(input("Digite um número: "))
    if num % 2 == 0 and num > 0:
        print("O número é par e positivo!")
    elif num % 2 == 0 and num < 0:
        print("O número é par e negativo!")
    elif num == 0:
        print("O número é zero!")
    elif num % 2 != 0 and num > 0:
        print("O número é ímpar e positivo!")
    else:
        print("O número é ímpar e negativo!")

if __name__ == "__main__":
    compostos()
