#Maior e menor numero part 2

numero_1 = int(input("Digite seu numero"))
numero_2 = int(input("Digite seu numero"))
numero_3 = int(input("Digite seu numero"))


import os 

os.system("clear") # Limpa o  terminal.

maior_numero = max (numero_1, numero_2, numero_3)
menor_numero = min (numero_1, numero_2, numero_3)

# Exibindo dados.
print()
print(f"Primeiro numero: {numero_1}")
print(f"primeiro numero: {numero_2}")
print(f"primeiro numero: {numero_3} ")
print()
print(f"maior numero: { maior_numero}")
print(f"numero: { menor_numero}")
