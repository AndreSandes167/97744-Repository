import os
from dataclasses import dataclass

os.system("cls || clear")
          
@dataclass
class pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = pessoa(
    nome = input("Digite o seu nome:"),
    idade = int("Digite sua idade"),
    peso = float("Digite seu peso"),
    altura = float("Digite sua altura:"),
    )


print()

pessoa2 = pessoa(
nome = input("DIgite seu nome: ")),
idade = int(input("DIgite sua idade")),
peso = float(input("Digite seu peso")),
altura = float(input("Digite sua altura")),
)

print("\n=DADOS DA PESSOA =")
print(f"Nome: (pessoa1.nome), idade: (pessoa1.idade), peso: {pessoa1.peso},altura")
print(f"Nome: (pessoa1.nome), idade: (pessoa1.idade), peso: {pessoa1.peso},altura")

