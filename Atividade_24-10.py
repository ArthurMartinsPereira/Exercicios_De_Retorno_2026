# Calcular Descontos:
d1 = 0.9
d2 = 0.7
d3 = 0.5

class Calcular:
    def __init__(self):
        self.valor = 0

    def calc(self):
        self.valor = float(input("Qual o valor do produto? "))
        desconto = input("Qual o desconto a ser aplicado?(10%,30%,50%)")
        if desconto == "10%":
            self.valor *= d1
            return self.valor
        elif desconto == "30%":
            self.valor *= d2
            return self.valor
        elif desconto == "50%":
            self.valor *= d3
            return self.valor
        else:
            return "Desconto invalido"

calculadora = Calcular()
resultado = calculadora.calc()
print(resultado)
