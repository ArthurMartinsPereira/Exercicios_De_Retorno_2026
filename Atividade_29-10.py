# Sistema de Cadastro de Produtos:

class Sistema:
    def __init__(self):
        self.produtos = []

    def options(self):
        while True:
            print("\n === Sistema de Produtos ===")
            print("1- Cadastrar produto")
            print("2- Listar produto")
            print("3- Buscar produto")
            print("4- Atualizar produto")
            print("5- Remover produto")
            print("6- Consultar valor total do estoque")
            print("0- Sair")
            try:
                c = int(input("Escolha uma opção: "))
                if c == 1:
                    self.cadastrar_produto()
                elif c == 2:
                    self.listar_produto()
                elif c == 3:
                    self.buscar_produto()
                elif c == 4:
                    self.atualizar_produto()
                elif c == 5:
                    self.remover_produto()
                elif c == 6:
                    self.consultar_estoque()
                elif c == 0:
                    break
                else:
                    print("Opção invalida!")

            except ValueError:
                print("Opção invalida!")

    def cadastrar_produto(self):
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade de produto: "))
        valor = float(input("Digite o valor do produto: "))
        novo_produto = {
            "produto": produto,
            "quantidade": quantidade,
            "valor": valor
        }
        self.produtos.append(novo_produto)
        print("Produto cadastrado com sucesso!")
        print(self.produtos)

    def listar_produto(self):
        pass
    def buscar_produto(self):
        pass
    def atualizar_produto(self):
        pass
    def remover_produto(self):
        pass
    def consultar_estoque(self):
        pass