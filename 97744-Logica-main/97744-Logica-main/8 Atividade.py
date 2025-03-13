import os

os.system("clear") # Limpa o terminal

numero_1 = int(input("Digite sua nota "))
numero_2 = int(input("Digite sua nota" ))

print(f"numero 1:  {numero_1}")
print(f"numero 2:  {numero_2}")

if numero_1 < numero_2:
    print(f"Maior numero e: {numero_2}")

elif numero_2 < numero_1:
    print(f"Maior numero e: {numero_1}")


if numero_1 < numero_2:
    print(f"Menor numero e: {numero_1}")

elif numero_2 < numero_1:
    print(f"Menor numero e: {numero_2}")


else: 
    print("sao iguais")
    

