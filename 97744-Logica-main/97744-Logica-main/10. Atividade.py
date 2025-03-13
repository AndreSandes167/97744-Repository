import os

os.system("clear")  # Limpa o terminal.

desejo = float(input("Digite seu numero: "))

maças = (1.30)
maças_2 = (1.00)

produto = (desejo * maças)

if desejo <= 12:
    print(desejo * maças)
else:    
    print(desejo * maças_2)
