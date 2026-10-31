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
        print("--- Produtos cadastrados ---")
        if not self.produtos:
            print("Nenhum produto cadastrado!")
            return
        for produto in self.produtos:
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade em estoque: {produto['quantidade']}")
            print(f"Valor unitário: R$ {produto['valor']:.2f}")
            print(f"Valor total do estoque: R$ {produto['valor'] * produto['quantidade']:.2f}")
        print(f"\n------------------------------")

    def buscar_produto(self):
        encontrado = False
        nome = input("Digite o nome do produto: ").lower()
        for produto in self.produtos:
            if produto["nome"].lower() == nome:
                encontrado = True
                print(produto)
        if not encontrado:
            print("Produto não encontrado!")

    def atualizar_produto(self):
        nome = input("Digite o nome do produto que deseja atualizar: ").lower()
        encontrado = False
        for produto in self.produtos:
            if produto["nome"].lower() == nome:
                encontrado = True
                print("Qual informação deseja atualizar?")
                print("1 - Nome")
                print("2 - Quantidade")
                print("3 - Valor")
                c = int(input("Escolha uma opção: "))
                if c == 1:
                    try:
                        new_nome = input("Digite o novo nome do produto: ")
                        if not new_nome.strip() == "":
                            produto["nome"] = new_nome
                            break
                        else:
                            print("Nome inválido!")
                    except ValueError:
                        print("Nome inválido!")

                elif c == 2:
                    try:
                        new_quant = int(input("Digite a nova quantidade de produto: "))
                        if new_quant >= 0:
                            produto["quantidade"] = new_quant
                            break
                        else:
                            print("Quantidade inválida!")
                    except ValueError:
                        print("Quantidade inválida!")

                elif c == 3:
                    try:
                        new_valor = float(input("Digite o novo valor do produto: "))
                        if new_valor >= 0:
                            produto["valor"] = new_valor
                            break
                        else:
                            print("Valor inválido!")
                    except ValueError:
                        print("Valor inválido!")
                else:
                    print("Opção invalida!")

        if not encontrado:
            print("Produto não encontrado!")


    def remover_produto(self):
        removido = False
        nome = input("Digite o nome do produto: ").lower()
        for produto in self.produtos:
            if produto["nome"].lower() == nome:
                self.produtos.remove(produto)
                removido = True
                break
        if removido:
            print("Produto removido com sucesso!")
        else:
            print("Produto não encontrado!")

    def consultar_estoque(self):
        val_estoque = 0
        for produto in self.produtos:
            val_estoque += produto["valor"] * produto["quantidade"]
        print(f"O valor total do estoque é: R${val_estoque}")
