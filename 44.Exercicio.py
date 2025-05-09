import os

os.system("cls || clear")


# Função para converter metros em centímetros
def metros_para_centimetros(metros):
    """
    Converte um valor de metros para centímetros.
    1 metro = 100 centímetros
    """
    return metros * 100

# Função para solicitar e validar a entrada do usuário
def solicitar_valor():
    """
    Solicita ao usuário um valor em metros e garante que seja um número positivo.
    Retorna o valor convertido para float.
    """
    while True:
        try:
            valor = float(input("Digite um valor em metros: "))
            if valor < 0:
                print("Por favor, digite um valor positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

# Programa principal
def main():
    """
    Função principal do programa.
    Solicita um valor ao usuário, converte para centímetros e exibe o resultado.
    """
    metros = solicitar_valor()  # Solicita o valor ao usuário
    centimetros = metros_para_centimetros(metros)  # Converte metros para centímetros
    print(f"{metros} metros equivalem a {centimetros} centímetros.")  # Exibe o resultado

# Executa o programa
if __name__ == "__main__":
    main()
