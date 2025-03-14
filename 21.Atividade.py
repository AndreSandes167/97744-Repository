import os
import time
os.system("clear") # Limpa o terminal.

media = 0
for i in range(4):
    numero = float(input("Digite suas notas: "))
    media += numero / 4
if media >= 7:
    print("Aprovado")
elif media <= 4:
    print("Reprovado")
else:
    print("Esta em recuperacao")
print(f"MEdia:  {media}")