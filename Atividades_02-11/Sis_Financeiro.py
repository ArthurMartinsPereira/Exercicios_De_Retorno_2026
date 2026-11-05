import json
from datetime import datetime

class Controle_Financeiro:
    def __init__(self):
        self.movimentacoes = []
        self.carregar_movimentacoes()

    def salvar_movimentacao(self):
        with open('movimentacoes.json', 'w', encoding="utf-8") as arquivo:
            json.dump(self.movimentacoes, arquivo, ensure_ascii=False, indent=4)

    def carregar_movimentacoes(self):
        try:
            with open('movimentacoes.json', 'r', encoding="utf-8") as arquivo:
                self.movimentacoes = json.load(arquivo)

        except FileNotFoundError:
            self.movimentacoes = []

        except json.JSONDecodeError:
            print("Arquivo danificado ou corrompido!")
            self.movimentacoes = []

    def options(self):
        while True:
            print("=== SISTEMA FINANCEIRO ===")
            print("1- Registrar Receita")
            print("2- Registrar Despesa")
            print("3- Listar Movimentações")
            print("4- Buscar Movimentações")
            print("5- Remover Movimentação")
            print("6- Consultar Saldo")
            print("7- Relatórios")
            print("0- Sair")

            try:
                c = int(input("Digite sua opcao: "))
                if c == 1:
                    self.registrar_movimentacao("receita")
                elif c == 2:
                    self.registrar_movimentacao("despesa")
                elif c == 3:
                    self.listar_movimentacoes()
                elif c == 4:
                    self.buscar_movimentacao()
                elif c == 5:
                    self.remover_movimentacao()
                elif c == 6:
                    self.consultar_saldo()
                elif c == 7:
                    self.relatorios()
                elif c == 0:
                    break
                else :
                    print("Opcao invalida!")

            except ValueError:
                print("Opcao invalida!")

    def registrar_movimentacao(self, tipo):
        while True:
            try:
                print("Registrar Movimentação: ")
                desc = input("Digite a descrição: ")
                categoria = input("Categoria da movimentação: ")
                valor = float(input("Valor da movimentação: "))
                data = input("Data da movimentação (DD/MM/AAAA): ")
                desc = desc.strip()
                categoria = categoria.strip()

                try:
                    data = datetime.strptime(data, "%d/%m/%Y")
                    data = data.strftime("%d/%m/%Y")
                except ValueError:
                    print("Data invalida!")
                    continue

                if valor <= 0 or desc.strip() == "" or categoria.strip() == "":
                    print("Valor inválido!")
                else:
                    break

            except ValueError:
                print("Registro invalido!")

        nova_movimentacao = {
            "desc": desc,
            "tipo": tipo,
            "categoria": categoria,
            "valor": valor,
            "data": data
        }
        print("Movimentação Registrada!")
        self.movimentacoes.append(nova_movimentacao)
        self.salvar_movimentacao()

    def listar_movimentacoes(self):
        print("---- Movimentações Cadastradas ----")
        if not self.movimentacoes:
            print("Nenhuma moviemntação cadastrada!")
            return
        for movimentacao in self.movimentacoes:
            print(f"Descrição: {movimentacao['desc']}")
            print(f"Tipo: {movimentacao['tipo']}")
            print(f"Categoria: {movimentacao['categoria']}")
            print(f"Valor: R${movimentacao['valor']:.2f}")
            print(f"Data: {movimentacao['data']}")
            print("\n---------------------------------")

    def buscar_movimentacao(self):
        pass

    def remover_movimentacao(self):
        pass

    def consultar_saldo(self):
        pass

    def relatorios(self):
        pass


sistema = Controle_Financeiro()
sistema.options()