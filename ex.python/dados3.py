newset = set()

ex1 = {1, 2, 2, 2, 3 ,3, 4, 5}

print(ex1)

ex2 = {j for j in range(10)}

print(ex2)

ex2.add(10)
ex2.add(50)
ex2.add(39)
ex2.add(21)
print(ex2)

ex3 = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8]

setagem = set(ex3)
print(setagem)

listagem = list(setagem)
print(listagem)

tupleagem = tuple(setagem)
print(tupleagem)