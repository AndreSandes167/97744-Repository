import os
os.system("cls || clear")

#função sem retorno.
#Definindo caracteristicas de função.
def saudação(nome):
    print(f"olá  {nome}! bem-vindo(a) ao curso de DS!")

    nome_visitante = "Marta"
    saudação(nome_visitante)


# crie uma função com o nome: disciplina(História) que receba o nome de 
# uma disciplina do curso de DS.
# Mostra o texto: A disciplina *** faz parte do curso de DS.
def disciplina (nome):
    print(f"A disciplina {nome} faz parte do curso de DS.")

    nome = input("Digite seu nome: ")
    nome_disciplina = input("Digite o nome da disciplina: ")


saudação("Marta") # chamando a função.
disciplina(nome_disciplina) # chamando a função.


