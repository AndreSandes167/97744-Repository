import os

from dataclasses import dataclass


os.system("cls || clear")



class Autor:
    def __init__(self, nome, biografia):
        self.nome = nome
        self.biografia = biografia


class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor  # autor é uma instância da classe Autor

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Ano de publicação: {self.ano}")
        print(f"Autor: {self.autor.nome}")


autor1 = Autor("Machado de Assis", "Escritor brasileiro do século XIX.")
livro1 = Livro("Dom Casmurro", 1899, autor1)


livro1.exibir_detalhes()

