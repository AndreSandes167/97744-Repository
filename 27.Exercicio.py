import os
os.system("cls || clear")

senha_cadastrado="1234"
login_cadastrado="deco"

while True:
    login=str(input("digite o usuario: ")).lower()
    senha=str(input("digite a senha: "))

    if senha==senha_cadastrado and login==login_cadastrado:
        print()
        print("login e senha corretas, seja bem vindo")
        break
    else:
        print()
        print("login ou senha incorretos, tente novamente")
        print()
print()
