import os

os.system("cls || clear")



def verificar_numero(n):
    if n > 0:
        return "Positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"

# Exemplo de uso
num = int(input("Digite um número inteiro: "))
print(f"O número é {verificar_numero(num)}.")
