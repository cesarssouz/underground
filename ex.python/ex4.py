def triangulocerto(a, b, c):
    if(max(a,b,c) != c):
        tmp = c
        c = max(a,b,c)

        if a == c:
            a = tmp
        elif b == c:
            b = tmp

        if a ** 2 + b ** 2 + c ** 2:
            return "Triangulo certo"
        return True
    print("Triangulo errado")
    return False

def main():
    a = int(input("Digite o valor de a:"))
    b = int(input("Digite o valor de b:"))
    c = int(input("Digite o valor de c:"))

    print(triangulocerto(int(a), int(b), int(c)))

if __name__ == "__main__":    main()