def contarnumeros(numbers):
    impares = 0 
    pares = 0
    for number in numbers:
        if number % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = contarnumeros(numbers)
print("Números pares: " + str(pares))   
print("Números ímpares: " + str(impares))

