import os 
from dataclasses import dataclass

# Limpa o terminal
os.system("cls || clear")

# Criando uma classe.
@dataclass
class pessoa:
    nome: str
    idade: int

 # Aplicando caracteristicas da classe.
pessoa1 = pessoa("Alice", 30)
pessoa2 = pessoa("Bob", 25)

# Aplicando caracteristicas da classe.
Pet1 = pet("Totó", 4, 7.8)
pet2 = pet("Tubarão", 6, 9.2)


print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade} anos.")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade} anos.")

print("\n"