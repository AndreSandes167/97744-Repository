import os

os.system("cls || clear")


def contar_pares(numeros):
    return sum(1 for num in numeros if num % 2 == 0)

def contar_impares(numeros):
    return sum(1 for num in numeros if num % 2 != 0)


numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(6)]


qtd_pares = contar_pares(numeros)
qtd_impares = contar_impares(numeros)

print(f"Quantidade de números pares: {qtd_pares}")
print(f"Quantidade de números ímpares: {qtd_impares}")
