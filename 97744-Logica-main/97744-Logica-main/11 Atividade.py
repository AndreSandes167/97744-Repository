import os

os.system("clear") # Limpa o terminal.

# solicitando dados 

numero_1 = float(input(Input("Digite um numero:" ))
numero_2 = float(input(Input("Digite um numero:" ))

print()
operador = input("Digite o operador: ")

if operador == "+":
    resultado = numero_1 + numero_2
    elif operador == "-":
        resultado = numero_1 - numero_2
    elif operador == "*":
        resultado = numero_1 * numero_2
     elif operador == "/":
        resultado = numero_1 / numero_2

    print()     
    print(f"primeiro numero: {numero_1}")
    print(f"segundo numero: {numero_2}")
    print(f"operador:  {operador}")  
    print(f" resultado: {resultado}")      