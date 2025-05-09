import os

os.system("cls || clear")

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Entrada de notas pelo usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = calcular_media(nota1, nota2)

# Exibição dos resultados
print(f"Média do aluno: {media:.2f}")
print(f"Situação: {verificar_aprovacao(media)}")
