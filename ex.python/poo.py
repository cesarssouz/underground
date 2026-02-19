class Livraria:
    pass

meulivro = Livraria()
print(meulivro)

print(type(meulivro))

print(isinstance(meulivro, Livraria))

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

livro1 = Livro("Como fazer amigos e influenciar pessoas", "Adrian", 1968)
print(livro1.titulo)
print(livro1.autor) 
print(livro1.ano)
