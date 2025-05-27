import os

from dataclasses import dataclass

os.system("cls || clear")


@dataclass
class funcionario:
    nome: str
    data_admisao: str
    matricula:str
    endereço: str

    def salvar_funcionarios(lista):
        nome_arquivo = "dados_funcionarios.csv"

        with open(nome_arquivo,  "a") as arquivo_funcionarios:
            for funcionarios.w

