entrada =(input("Digite numeros separados por virgula: "))
lista_str = entrada.split(",")
numeros = [int(num) for num in lista_str]

resultado = {
    "maior": max(numeros),
    "menor": min(numeros), 
    "total":len(numeros),
    "pares": [num for num in numeros if num % 2 == 0],
    "impares": [num for num in numeros if num % 2 != 0]
}

print(resultado)