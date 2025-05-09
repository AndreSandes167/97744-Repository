import os

os.system("cls|| clear")


#resultando dados

contador = 0
soma = 0

while True:
    nota = float(input("Digite uma nota: "))
    soma += nota
    contador += 1

    continuar = input("Deseja inserir mais uma nota? (S/N): ").strip().upper()
    if continuar == "N":
        break

media = soma / contador
print(f"A média aritmética das notas informadas é: {media:.2f}")


