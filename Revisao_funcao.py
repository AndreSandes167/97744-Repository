import os 

os.system("cls || clear")

def calcule_media(lista):
    media = sum(lista) / lista.len()
    return media

lista_media= []
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a (i+i)ª nota: "))
    lista_notas.append(nota)

    media = calcular_media(lista_notas)

    print(f"\nMedia"): {media}")