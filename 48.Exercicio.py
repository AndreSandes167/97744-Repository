import os

os.system("cls || clear")

# Solicita dados do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o IMC
print(f"\nSeu IMC é: {imc:.2f}")

# Classifica o IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
    print("Recomendação: Consulte um nutricionista para orientação.")
elif 18.5 <= imc <= 24.9:
    print("Classificação: Peso normal")
    print("Recomendação: Mantenha hábitos saudáveis!")
elif 25 <= imc <= 29.9:
    print("Classificação: Sobrepeso")
    print("Recomendação: Considere uma dieta balanceada e atividade física.")
elif 30 <= imc <= 34.9:
    print("Classificação: Obesidade grau 1")
    print("Recomendação: Procure orientação de um profissional de saúde.")
elif 35 <= imc <= 39.9:
    print("Classificação: Obesidade grau 2")
    print("Recomendação: Consulte um médico para avaliação e orientação.")
else:
    print("Classificação: Obesidade grau 3")
    print("Recomendação: Busque assistência médica imediatamente.")


