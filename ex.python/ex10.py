def numero():

    usernum = int(input("Digite um número: "))
    if usernum % 2 == 0:
        print("O número é par e divido por 2 fica " + str(usernum // 2))
    else:
        print("O número é ímpar e multiplicado por 3 fica e somando com 1 fica " + str(usernum * 3 + 1))

if __name__ == "__main__":
    numero()




