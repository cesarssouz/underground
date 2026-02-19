list = []

list2 = ["Hello", "John", "Kaisen"]

print("Primeiro elemnto é: " + list2[0])
print("Segundo elemnto é: " + list2[1])

list2.insert(1, "World ")
print(list2)

list2.append("Bye")
print(list2)

list2.remove("World ")
print(list2)

list2.pop()
print(list2)

list2.sort()
print(list2)

print("O número de elementos na lista é: " + str(len(list2)))
print("O número de elementos na lista é: " + str(len(list)))

"".join(list2)

print(list2)