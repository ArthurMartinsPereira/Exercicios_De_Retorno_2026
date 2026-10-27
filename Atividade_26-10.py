# Analizador de Texto:

class Analyze:
    def text(self):
        frase = input("Digite uma frase: ")
        palavras = frase.split()
        vogais = "aeiouáéíóúãõâêô"
        v = 0
        espacos = frase.count(" ")
        print (f"Quantidade de caracteres: {len(frase)}")
        print (f"Quantidade de palavras: {len(palavras)}")
        for letra in frase.lower():
            if letra in vogais:
                v += 1
        print(f"Número de vogais: {v}")
        print (f"Quantidade de espaços: {espacos}")

analizar = Analyze()
analizar.text()