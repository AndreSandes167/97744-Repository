import os

os.system("clear")

algarismo_A = int(input("digite o valor A: "))
algarismo_B = int(input("digite o valor B: "))
algarismo_C = int(input("digite o valor C:"))

soma = (algarismo_A + algarismo_B)

print()

if soma < algarismo_C:
    print(" A + B é menor que C")

else:
    print("A + B é maior que C")
    

