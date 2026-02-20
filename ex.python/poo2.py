class Armario():
    def __init__(self, gaveta1, gaveta2, gaveta3, gaveta4):
        self.gaveta1 = gaveta1
        self.gaveta2 = gaveta2
        self.gaveta3 = gaveta3
        self.gaveta4 = gaveta4

    def abrir_gaveta1(self):
        return "{} {}: {}".format(self.gaveta1, self.gaveta2, self.gaveta3)
    
    def __str__(self):
        return "{} {}: ({})".format(self.gaveta1, self.gaveta2, self.gaveta3, self.gaveta4)
    
    def __repr__(self):
        return "<gaveta: {} {} {} ({})>".format(self.gaveta1, self.gaveta2, self.gaveta3, self.gaveta4)


new_armario = Armario("Gaveta 1", "Gaveta 2", "Gaveta 3", "Gaveta 4")

print(new_armario.abrir_gaveta1())
