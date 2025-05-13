import os

from dataclasses import dataclass

os.system("cls||clear")

class Funcionario:
    def __init__(self, nome, data_nascimento, rg, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.rg = rg
        self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}, RG: {self.rg}, CPF: {self.cpf}"


def coletar_dados_funcionarios(quantidade=5):
    funcionarios = []
    for i in range(quantidade):
        print(f"\nInforme os dados do funcionário {i + 1}:")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        rg = input("RG: ")
        cpf = input("CPF: ")
        funcionario = Funcionario(nome, data_nascimento, rg, cpf)
        funcionarios.append(funcionario)
    return funcionarios


def salvar_em_arquivo(funcionarios, nome_arquivo="Funcionarios.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for f in funcionarios:
            linha = f"{f.nome};{f.data_nascimento};{f.rg};{f.cpf}\n"
            arquivo.write(linha)


def ler_e_mostrar_arquivo(nome_arquivo="Funcionarios.txt"):
    print("\nFuncionários salvos no arquivo:")
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, data_nascimento, rg, cpf = linha.strip().split(";")
                print(f"Nome: {nome}, Data de Nascimento: {data_nascimento}, RG: {rg}, CPF: {cpf}")
    except FileNotFoundError:
        print("Arquivo não encontrado.")


# Execução do programa
funcionarios = coletar_dados_funcionarios()
salvar_em_arquivo(funcionarios)
ler_e_mostrar_arquivo()
