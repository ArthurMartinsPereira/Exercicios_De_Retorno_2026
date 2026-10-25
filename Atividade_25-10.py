# Calculadora de Descontos Flexivel

class Calculadora:
    def __init__(self):
        self.valor = 0

    def calcular(self):
        self.valor = float(input("Digite o valor a ser pago: "))
        desconto = int(input("Desconto a ser aplicado(%): "))
        self_desc = self.valor * (desconto / 100)
        self.valor = self.valor - self_desc
        print(f"O valor com desconto é {self.valor}")

calculadora = Calculadora()
calculadora.calcular()