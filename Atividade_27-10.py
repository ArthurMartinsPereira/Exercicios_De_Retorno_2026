# Central de Utilidades

class Central:
    def choice(self):
        while (True):
            print("=== Central de Utilidades ===")
            print("1- Analizar Texto")
            print("2- Calcular Desconto")
            print("3- Converter Temperatura")
            print("0- Sair")
            c = int(input("Escolha uma opcao: "))
            if c == 1:
                self.analizar_texto()
            elif c == 2:
                self.calc_desconto()
            elif c == 3:
                self.conv_temp()
            elif c == 0:
                return 0
            else:
                print("Opcao invalida")

    def analizar_texto(self):
        frase = input("Digite uma frase: ")
        palavras = frase.split()
        vogais = "aeiouáéíóúãõâêô"
        v = 0
        espacos = frase.count(" ")
        print("Quantidade de palavras: ", len(palavras))
        print("Quantidade de Caracteres: ", len(frase))
        for letra in frase.lower():
            if letra in vogais:
                v += 1
        print("Quantidade de vogais: ", v)
        print("Quantidade de espacos: ", espacos)

    def calc_desconto(self):
        valor = float (input("Digite um valor: "))
        desconto = int(input("Digite o desconto(%): "))
        if 0 < desconto < 100:
            self_desc = valor * (desconto / 100)
            valor_original = valor
            valor = valor - self_desc

            print(f"O valor com desconto é: {valor:.2f}")
            print(f"O valor original é: {valor_original:.2f}")
        else:
            print("Desconto invalido...")

    def conv_temp(self):

central = Central()
central.choice()