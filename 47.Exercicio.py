import os

os.system("cls || clear")

import math


def calcular_media(notas):
    return math.floor(sum(notas) / len(notas))

notas = []
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = calcular_media(notas)
print(f"A média arredondada para baixo é: {media}")
