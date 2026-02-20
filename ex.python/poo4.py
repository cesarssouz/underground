class animal:
    pass

class fish(animal):
    def speak (self):
        return "Blub blub"
    
class peixepalhaco(fish):
    def speak(self):
        return "Blub blub, I'm a clownfish"
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "A clowfished named " + self.name
class peixeespada(fish):
    pass

doke = peixepalhaco('Doke')
print(doke.speak())
print(doke)

spike = peixeespada()
print(spike.speak())

