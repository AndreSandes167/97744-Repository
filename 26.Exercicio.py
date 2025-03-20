import os
os.system("cls || clear")
# Atividade com laço de repetição while.
soma = 0
Quantidade_Notas= 2
for i in range(Quantidade_Notas):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida, tente novamente.\n")
        else:
            soma += nota
            break

media = soma / Quantidade_Notas

print(f"Media: {media}")