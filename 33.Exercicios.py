import os

os.system("cls || clear ")

def main():
    familias = []
    
    while True:
        print("\nMenu:")
        print("1 - Adicionar família")
        print("2 - Sair e exibir resultados")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            salario = float(input("Digite o salário da família: "))
            num_filhos = int(input("Digite o número de filhos: "))
            familias.append((salario, num_filhos))
        
        elif opcao == "2":
            if not familias:
                print("Nenhuma família cadastrada.")
                break
            
            total_familias = len(familias)
            media_salario = sum(f[0] for f in familias) / total_familias
            media_filhos = sum(f[1] for f in familias) / total_familias
            maior_salario = max(f[0] for f in familias)
            menor_salario = min(f[0] for f in familias)

            print("\nResultados da pesquisa:")
            print(f"Total de famílias: {total_familias}")
            print(f"Média salarial: R$ {media_salario:.2f}")
            print(f"Média de filhos: {media_filhos:.2f}")
            print(f"Maior salário: R$ {maior_salario:.2f}")
            print(f"Menor salário: R$ {menor_salario:.2f}")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
