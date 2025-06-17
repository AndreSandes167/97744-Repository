import os
from dataclasses import dataclass
os.system("Cls || clear")

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def __str__(self):
        status = "Emprestado" if self.emprestado else "Disponível"
        return f"Título: {self.titulo}, Autor: {self.autor}, Status: {status}"

class Biblioteca:
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, titulo, autor):
        novo_livro = Livro(titulo, autor)
        self.acervo.append(novo_livro)
        print(f"Livro '{titulo}' de '{autor}' adicionado ao acervo.")

    def listar_todos_livros(self):
        if not self.acervo:
            print("O acervo da biblioteca está vazio.")
            return

        print("\n--- LIVROS NO ACERVO ---")
        for i, livro in enumerate(self.acervo):
            print(f"{i+1}. {livro}")
        print("------------------------")

    def buscar_livro(self, termo_busca):
        resultados = []
        termo_lower = termo_busca.lower()
        for livro in self.acervo:
            if termo_lower in livro.titulo.lower() or \
               termo_lower in livro.autor.lower():
                resultados.append(livro)
        return resultados

    def emprestar_devolver_livro(self, titulo_livro, acao):
        livro_encontrado = None
        for livro in self.acervo:
            if livro.titulo.lower() == titulo_livro.lower():
                livro_encontrado = livro
                break

        if not livro_encontrado:
            print(f"Livro com título '{titulo_livro}' não encontrado no acervo.")
            return

        if acao == 'emprestar':
            if not livro_encontrado.emprestado:
                livro_encontrado.emprestado = True
                print(f"Livro '{livro_encontrado.titulo}' emprestado com sucesso!")
            else:
                print(f"Livro '{livro_encontrado.titulo}' já está emprestado.")
        elif acao == 'devolver':
            if livro_encontrado.emprestado:
                livro_encontrado.emprestado = False
                print(f"Livro '{livro_encontrado.titulo}' devolvido com sucesso!")
            else:
                print(f"Livro '{livro_encontrado.titulo}' não estava emprestado.")
        else:
            print("Ação inválida. Por favor, use 'emprestar' ou 'devolver'.")

def exibir_menu():
    print("\n=== SISTEMA DE GESTÃO DE BIBLIOTECA ===")
    print("1. Adicionar Novo Livro")
    print("2. Listar Todos os Livros")
    print("3. Buscar Livro")
    print("4. Emprestar/Devolver Livro")
    print("5. Sair")
    print("=======================================")

def main():
    minha_biblioteca = Biblioteca()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            minha_biblioteca.adicionar_livro(titulo, autor)

        elif opcao == '2':
            minha_biblioteca.listar_todos_livros()

        elif opcao == '3':
            termo = input("Digite o título ou autor para buscar: ")
            resultados = minha_biblioteca.buscar_livro(termo)
            if resultados:
                print("\n--- LIVROS ENCONTRADOS ---")
                for livro in resultados:
                    print(livro)
                print("--------------------------")
            else:
                print("Nenhum livro encontrado com o termo informado.")

        elif opcao == '4':
            titulo_livro = input("Digite o título do livro para emprestar/devolver: ")
            acao = input("Digite 'emprestar' ou 'devolver': ").lower()
            minha_biblioteca.emprestar_devolver_livro(titulo_livro, acao)

        elif opcao == '5':
            print("Saindo do sistema. Volte sempre!")
            break
        else:
            print("Opção inválida. Por favor, digite um número de 1 a 5.")

if __name__ == "__main__":
    main()
