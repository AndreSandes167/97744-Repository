import os

os.system("cls || clear")

class Funcionario:
    def __init__(self, nome, data_nascimento, cpf, funcao):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.funcao = funcao

    def __str__(self):
        return f"Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}, CPF: {self.cpf}, Função: {self.funcao}"


# Lista para armazenar os funcionários
funcionarios = []


def menu():
    print("\n--- Menu ---")
    print("1. Adicionar funcionário")
    print("2. Listar funcionários")
    print("3. Atualizar funcionário")
    print("4. Remover funcionário")
    print("5. Sair")


def adicionar_funcionario():
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    cpf = input("CPF: ")
    funcao = input("Função: ")
    funcionario = Funcionario(nome, data_nascimento, cpf, funcao)
    funcionarios.append(funcionario)
    print("Funcionário adicionado com sucesso!")


def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        for i, func in enumerate(funcionarios):
            print(f"{i + 1}. {func}")


def atualizar_funcionario():
    listar_funcionarios()
    try:
        indice = int(input("Digite o número do funcionário que deseja atualizar: ")) - 1
        if 0 <= indice < len(funcionarios):
            nome = input("Novo nome: ")
            data_nascimento = input("Nova data de nascimento: ")
            cpf = input("Novo CPF: ")
            funcao = input("Nova função: ")
            funcionarios[indice] = Funcionario(nome, data_nascimento, cpf, funcao)
            print("Funcionário atualizado com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")


def remover_funcionario():
    listar_funcionarios()
    try:
        indice = int(input("Digite o número do funcionário que deseja remover: ")) - 1
        if 0 <= indice < len(funcionarios):
            funcionarios.pop(indice)
            print("Funcionário removido com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")


# Loop principal
while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        adicionar_funcionario()
    elif escolha == '2':
        listar_funcionarios()
    elif escolha == '3':
        atualizar_funcionario()
    elif escolha == '4':
        remover_funcionario()
    elif escolha == '5':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")


