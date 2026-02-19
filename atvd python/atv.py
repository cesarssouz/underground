def numeromaior():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    result = max(num1, num2, num3)
    print("O maior número é: " + str(result))

if __name__ == "__main__":
    numeromaior()