import os

os.system("cls || clear")

numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)


    print("Números informados:", numeros)

    menor = min(numeros)
    maior = max(numeros)


    print("Menor numero:", menor)
    print("Maior número:", maior)
          