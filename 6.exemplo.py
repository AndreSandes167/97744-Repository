import os

from dataclasses import dataclass

os.system("cls || clear")

import json

# Classe para Funcionário
class Funcionario:
    def __init__(self, nome, data_admissao, matricula, endereco):
        self.nome = nome
        self.data_admissao = data_admissao
        self.matricula = matricula
        self.endereco = endereco

    def to_dict(self):
        return {
            "nome": self.nome,
            "data_admissao": self.data_admissao,
            "matricula": self.matricula,
            "endereco": self.endereco
        }

# Classe para Cliente
class Cliente:
    def __init__(self, nome, data_nascimento, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def to_dict(self):
        return {
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "endereco": self.endereco
        }

# Função para coletar dados de funcionários
def coletar_funcionarios():
    funcionarios = []
    for i in range(3):
        print(f"\nInforme os dados do Funcionário {i+1}")
        nome = input("Nome: ")
        data_admissao = input("Data de admissão (dd/mm/aaaa): ")
        matricula = input("Matrícula: ")
        endereco = input("Endereço: ")
        funcionario = Funcionario(nome, data_admissao, matricula, endereco)
        funcionarios.append(funcionario)
    return funcionarios

# Função para coletar dados de clientes
def coletar_clientes():
    clientes = []
    for i in range(3):
        print(f"\nInforme os dados do Cliente {i+1}")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        endereco = input("Endereço: ")
        cliente = Cliente(nome, data_nascimento, endereco)
        clientes.append(cliente)
    return clientes

# Função para salvar lista de objetos em arquivo JSON
def salvar_em_arquivo(nome_arquivo, lista_objetos):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump([obj.to_dict() for obj in lista_objetos], f, ensure_ascii=False, indent=4)
    print(f"\nDados salvos em '{nome_arquivo}' com sucesso.")

# Execução principal
def main():
    funcionarios = coletar_funcionarios()
    clientes = coletar_clientes()
    salvar_em_arquivo("funcionarios.json", funcionarios)
    salvar_em_arquivo("clientes.json", clientes)

if __name__ == "__main__":
    main()

