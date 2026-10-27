# Calculadora de Descontos Flexivel:

class Calculadora:
    def __init__(self):
        self.valor = 0

    def calcular(self):
        self.valor = float(input("Digite o valor a ser pago: "))
        desconto = int(input("Desconto a ser aplicado(%): "))
        self_desc = self.valor * (desconto / 100)
        valor_original = self.valor
        self.valor = self.valor - self_desc
        if 0 < desconto < 100:
            print(f"O valor com desconto é {self.valor:.2f}")
            print(f"O valor original é {valor_original}")
        else:
            print("Desconto Invalido!")

calculadora = Calculadora()
calculadora.calcular()