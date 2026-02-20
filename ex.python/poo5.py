class vertebrado:
    pass

class fish(vertebrado):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is {}".format(self.name)
    
class peixepalhaco(fish):
    def __init__(self, name):
        self.name = name

doke = peixepalhaco('Doke')
print(doke)