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
        while True:
            try:
                nome = input("Digite o nome do produto: ")
                quantidade = int(input("Digite a quantidade de produto: "))
                valor = float(input("Digite o valor do produto: "))
                if nome.strip() == "" or quantidade < 0 or valor < 0:
                    print("Dados invalidos!")
                else:
                    break
            except ValueError:
                print("Informação invalida!")

        novo_produto = {
            "nome": nome,
            "quantidade": quantidade,
            "valor": valor
        }
        self.produtos.append(novo_produto)
        print("Produto cadastrado com sucesso!")

    def listar_produto(self):
        print("Produtos cadastrados:")
        for produto in self.produtos:
            print(produto)
        print("---------------")

    def buscar_produto(self):
        encontrado = False
        nome = input("Digite o nome do produto: ").lower()
        for produto in self.produtos:
            if produto["nome"] == nome:
                encontrado = True
                print(produto)
        if not encontrado:
            print("Produto não encontrado!")

    def atualizar_produto(self):
        nome = input("Digite o nome do produto que deseja atualizar: ").lower()
        print("Qual informação deseja atualizar?")
        print("1 - Nome")
        print("2 - Quantidade")
        print("3 - Valor")
        c = int(input("Escolha uma opção: "))
        if c == 1:



    def remover_produto(self):
        removido = False
        nome = input("Digite o nome do produto: ").lower()
        for produto in self.produtos:
            if produto["nome"] == nome:
                self.produtos.remove(produto)
                removido = True
                break
        if removido:
            print("Produto removido com sucesso!")
        else:
            print("Produto não encontrado!")

    def consultar_estoque(self):
        pass