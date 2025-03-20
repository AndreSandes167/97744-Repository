import os
os.system("clls || clear")

# Exemplo de uso do laço de repetição while.
idade = int(input("Digite sua idade: "))

while idade < 18:
    print("não autorizo.  \nsomente maiores de 18. \n")
    idade = int(input("Digite sua idade: "))

print("Acesso permitido. ")
print("fim.")
