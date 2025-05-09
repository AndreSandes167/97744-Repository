class Endereco:
    def __init__(self, logradouro, numero, cidade):
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def mostrar_endereco(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}"


class Usuario:
    def __init__(self, nome, email, endereco):
        self.nome = nome
        self.email = email
        self.endereco = endereco

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco.mostrar_endereco()}")


# Solicitando dados do usuário
nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")
logradouro = input("Digite o logradouro: ")
numero = input("Digite o número: ")
cidade = input("Digite a cidade: ")

# Criando objetos
endereco = Endereco(logradouro, numero, cidade)
usuario = Usuario(nome, email, endereco)

# Mostrando os dados
print("\nDados do usuário:")
usuario.mostrar_dados()
