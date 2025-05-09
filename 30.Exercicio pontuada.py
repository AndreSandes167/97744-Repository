contador = 0
soma = 0

while True:
    numero = int(input("Digite um número inteiro positivo (ou um número negativo para sair): "))
    
    if numero < 0:
        break  # Interrompe o loop se o número for negativo
    
    soma += numero
    contador += 1

# Evita divisão por zero
if contador > 0:
    media = soma / contador
    print(f"A média aritmética dos números informados é: {media:.2f}")
else:
    print("Nenhum número válido foi inserido.")
