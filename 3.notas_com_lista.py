import os

os.system("cls || clear")

lista_notas = [] # Criando uma lista

for i in range(3):
    nota = float(input("Digite uma nota: "))
    lista_notas.apped(nota)

    media = sum(lista_notas) / 3

    # Mostrando cada nota informada.
    print()
    for nota in lista_notas: # forEach
        print(f"Nota: {nota}")

print()
print(f"Média: {media}")

print()
print(f"somente a segunda nota: {lista_notas[1]}")
