# -*- coding: utf-8 -*-
"""
Sistema de Gerenciamento de Biblioteca

Este programa simples simula um sistema de biblioteca com funcionalidades
para cadastrar, listar, buscar, emprestar e devolver livros.
"""

# Lista para armazenar os livros. Cada livro será um dicionário.
biblioteca = []

def cadastrar_livro():
    """
    Cadastra um novo livro na biblioteca.
    Solicita ao usuário o título, autor e ano de publicação do livro.
    O status inicial do livro é 'disponível'.
    """
    print("\n--- Cadastrar Novo Livro ---")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    while True:
        try:
            ano = int(input("Digite o ano de publicação: "))
            break
        except ValueError:
            print("Ano inválido. Por favor, digite um número.")

    # Verifica se o livro já existe (pelo título e autor para simplificar)
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower() and livro['autor'].lower() == autor.lower():
            print(f"Erro: O livro '{titulo}' do autor '{autor}' já está cadastrado.")
            return

    livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'status': 'disponível'  # Status pode ser 'disponível' ou 'emprestado'
    }
    biblioteca.append(livro)
    print(f"Livro '{titulo}' cadastrado com sucesso!")

def listar_livros():
    """
    Lista todos os livros cadastrados na biblioteca.
    Exibe o título, autor, ano e status de cada livro.
    """
    print("\n--- Lista de Livros ---")
    if not biblioteca:
        print("Nenhum livro cadastrado na biblioteca.")
        return

    print(f"{'ID':<5} | {'Título':<30} | {'Autor':<25} | {'Ano':<6} | {'Status':<12}")
    print("-" * 85)
    for i, livro in enumerate(biblioteca):
        print(f"{i:<5} | {livro['titulo']:<30} | {livro['autor']:<25} | {livro['ano']:<6} | {livro['status'].capitalize():<12}")
    print("-" * 85)

def buscar_livro_por_titulo():
    """
    Busca livros na biblioteca pelo título.
    A busca não diferencia maiúsculas de minúsculas.
    Exibe os livros encontrados ou uma mensagem se nenhum for encontrado.
    """
    print("\n--- Buscar Livro por Título ---")
    if not biblioteca:
        print("Nenhum livro cadastrado para buscar.")
        return

    termo_busca = input("Digite o título (ou parte do título) do livro a buscar: ").lower()
    livros_encontrados = []

    for i, livro in enumerate(biblioteca):
        if termo_busca in livro['titulo'].lower():
            livros_encontrados.append((i, livro))

    if not livros_encontrados:
        print(f"Nenhum livro encontrado com o título contendo '{termo_busca}'.")
    else:
        print("\n--- Livros Encontrados ---")
        print(f"{'ID':<5} | {'Título':<30} | {'Autor':<25} | {'Ano':<6} | {'Status':<12}")
        print("-" * 85)
        for i, livro in livros_encontrados:
            print(f"{i:<5} | {livro['titulo']:<30} | {livro['autor']:<25} | {livro['ano']:<6} | {livro['status'].capitalize():<12}")
        print("-" * 85)
    return livros_encontrados


def emprestar_devolver_livro():
    """
    Permite emprestar ou devolver um livro.
    O usuário primeiro busca o livro e depois escolhe a ação.
    """
    print("\n--- Emprestar/Devolver Livro ---")
    if not biblioteca:
        print("Nenhum livro cadastrado para emprestar ou devolver.")
        return

    livros_encontrados = buscar_livro_por_titulo() # Reutiliza a função de busca

    if not livros_encontrados:
        return # Mensagem de "não encontrado" já foi dada pela função buscar_livro_por_titulo

    if len(livros_encontrados) > 1:
        while True:
            try:
                id_selecionado_str = input("Múltiplos livros encontrados. Digite o ID do livro que deseja alterar o status: ")
                id_selecionado = int(id_selecionado_str)
                # Verifica se o ID selecionado está na lista de encontrados
                livro_valido = False
                for i, l in livros_encontrados:
                    if i == id_selecionado:
                        livro_para_alterar = biblioteca[id_selecionado]
                        livro_valido = True
                        break
                if livro_valido:
                    break
                else:
                    print("ID inválido. Por favor, escolha um ID da lista acima.")
            except ValueError:
                print("ID inválido. Por favor, digite um número.")
            except IndexError:
                 print("ID fora do intervalo. Por favor, escolha um ID da lista acima.")
    elif len(livros_encontrados) == 1:
        id_selecionado = livros_encontrados[0][0]
        livro_para_alterar = biblioteca[id_selecionado]
    else: # Nenhuma outra condição, mas por segurança
        return

    print(f"\nLivro selecionado: '{livro_para_alterar['titulo']}' (Status atual: {livro_para_alterar['status']})")

    while True:
        acao = input("Deseja (E)mprestar ou (D)evolver este livro? (E/D): ").upper()
        if acao == 'E':
            if livro_para_alterar['status'] == 'disponível':
                livro_para_alterar['status'] = 'emprestado'
                print(f"Livro '{livro_para_alterar['titulo']}' emprestado com sucesso.")
            else:
                print(f"Livro '{livro_para_alterar['titulo']}' já está emprestado.")
            break
        elif acao == 'D':
            if livro_para_alterar['status'] == 'emprestado':
                livro_para_alterar['status'] = 'disponível'
                print(f"Livro '{livro_para_alterar['titulo']}' devolvido com sucesso.")
            else:
                print(f"Livro '{livro_para_alterar['titulo']}' já está disponível.")
            break
        else:
            print("Opção inválida. Digite 'E' para emprestar ou 'D' para devolver.")

def menu_principal():
    """
    Exibe o menu principal e gerencia a interação do usuário.
    """
    while True:
        print("\n--- Sistema de Biblioteca ---")
        print("1. Cadastrar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro por Título")
        print("4. Emprestar/Devolver Livro")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            buscar_livro_por_titulo()
        elif opcao == '4':
            emprestar_devolver_livro()
        elif opcao == '5':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    # Adicionando alguns livros de exemplo para facilitar o teste
    biblioteca.append({'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien', 'ano': 1954, 'status': 'disponível'})
    biblioteca.append({'titulo': 'Dom Quixote', 'autor': 'Miguel de Cervantes', 'ano': 1605, 'status': 'emprestado'})
    biblioteca.append({'titulo': '1984', 'autor': 'George Orwell', 'ano': 1949, 'status': 'disponível'})
    biblioteca.append({'titulo': 'Cem Anos de Solidão', 'autor': 'Gabriel García Márquez', 'ano': 1967, 'status': 'disponível'})

    menu_principal()
    menu_principal()
