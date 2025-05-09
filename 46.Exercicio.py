import os

os.system("cls || clear")

import math


# Função para calcular a média e arredondar
def calcular_media(notas):
    return round(sum(notas) / len(notas))

# Leitura das notas
notas = []
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = calcular_media(notas)
print(f"A média arredondada é: {media}")
