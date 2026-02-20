class peixe:
    pass

nemo = peixe()
print(type(nemo))

print(isinstance(nemo, peixe))

class animal:
    pass

class vertebrado(animal):
    pass

class fish(vertebrado):
    pass

class peixepalhaco(fish):
    pass

class peixeespada(fish):
    pass

doke = peixepalhaco()
print(isinstance(doke, peixepalhaco))

print(isinstance(doke, peixeespada))

print(isinstance(doke, animal))

print(isinstance(doke, object))