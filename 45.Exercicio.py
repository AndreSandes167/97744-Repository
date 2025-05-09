import os

os.system("cls || clear")

# função para calcular a média 

def calcular_media(notas):
    return sum(notas) / len(notas)

# Lista para armazenar as notas 
notas = []

# Laço de repetição para ler 3 notas 
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}:"))
    notas.append(notas)

    # calcula e exibe a média
    media = calcular_media(notas)
    print(f"A média do aluno é: {media:.2f}")
