import json
from datetime import datetime

class Controle_Financeiro:
    def __init__(self):
        self.movimentacoes = []

    def salvar_movimentacao(self):
        with open('movimentacoes.json', 'w', encoding="utf-8") as arquivo:
            json.dump(self.movimentacoes, arquivo, ensure_ascii=False, indent=4)

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

                try:
                    data = datetime.strptime(data, "%d/%m/%y")
                except ValueError:
                    print("Data invalida!")

                if valor < 0 or desc.strip() == "" or categoria.strip() == "":
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