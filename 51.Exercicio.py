import os

os.system("cls || clear")


# Cardápio do restaurante
cardapio = {
    1: ("Picanha", 25.00),
    2: ("Lasanha", 20.00),
    3: ("Strogonoff", 18.00),
    4: ("Bife Acebolado", 15.00),
    5: ("Pão com ovo", 5.00)
}

pedidos = []

def mostrar_cardapio():
    print("Cardápio:")
    for codigo, (prato, valor) in cardapio.items():
        print(f"{codigo} - {prato} R$ {valor:.2f}")

# Loop para escolher os pratos
while True:
    mostrar_cardapio()
    try:
        escolha = int(input("Digite o código do prato desejado: "))
        if escolha in cardapio:
            pedidos.append(cardapio[escolha])
            print(f"{cardapio[escolha][0]} adicionado ao pedido.\n")
        else:
            print("Código inválido. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")

    continuar = input("Deseja escolher outro prato? (s/n): ").strip().lower()
    if continuar != 's':
        break

# Calcular total
total = sum(preco for _, preco in pedidos)

# Perguntar sobre a gorjeta
gorjeta = 0
deseja_gorjeta = input("Deseja pagar 10% de gorjeta para o garçom? (s/n): ").strip().lower()
if deseja_gorjeta == 's':
    gorjeta = total * 0.10

# Mostrar resumo
print("\nResumo do pedido:")
for prato, preco in pedidos:
    print(f"{prato} - R$ {preco:.2f}")

print(f"\nTotal dos pratos: R$ {total:.2f}")
print(f"Gorjeta: R$ {gorjeta:.2f}")
print(f"Valor total a pagar: R$ {total + gorjeta:.2f}")
