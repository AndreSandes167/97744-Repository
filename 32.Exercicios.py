import os

os.system("cls || clear")

def menu():
    print("\nMenu:")
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados")
    print("3 - Sair")

def coletar_dados():
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    salario = float(input("Salário: "))
    return idade, sexo, salario

def calcular_estatisticas(pessoas):
    if not pessoas:
        print("Nenhum dado cadastrado.")
        return
    
    salarios = [p[2] for p in pessoas]
    idades = [p[0] for p in pessoas]
    mulheres_com_alto_salario = sum(1 for p in pessoas if p[1] == 'F' and p[2] >= 5000)
    
    print("\nResultados:")
    print(f"Média salarial: R$ {sum(salarios) / len(salarios):.2f}")
    print(f"Maior idade: {max(idades)}")
    print(f"Menor idade: {min(idades)}")
    print(f"Quantidade de mulheres com salário >= R$ 5.000,00: {mulheres_com_alto_salario}")

def main():
    pessoas = []
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            pessoas.append(coletar_dados())
            print("\nPessoa adicionada com sucesso!")
        elif opcao == '2':
            calcular_estatisticas(pessoas)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
        
        input("Pressione Enter para continuar...")
        print("\033[H\033[J", end="")  # Limpa o terminal

if __name__ == "__main__":
    main()
