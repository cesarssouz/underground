import string 

def palindromo(text):
    excluir = set(string.punctuation )
    texto = ''.join(ch for ch in text if ch not in excluir)
    texto = texto.replace(" ", "").lower()

    if text == text[::-1]:
        return True
    else:        
        return False


def main():
        texto = input("Fala uma coisa ai: ")
        if palindromo(texto):
            print("É um palíndromo")
        else:
            print("Não é um palíndromo")

if __name__ == "__main__":    
    main()
