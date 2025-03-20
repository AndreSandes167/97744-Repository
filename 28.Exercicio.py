import os
os.system("cls || clear")
#dados pre colocados
senha_cadastrada="1234"
login_cadastrada="deco"
contador=0
for i in range(3):

    login=(input("digite o usuario ")).lower()
    senha=str(input("digite a senha "))

    if senha==senha_cadastrada and login==login_cadastrada:
#caso o login e senha sejam corretos
     print()
     print("login e senha corretas, seja bem vindo")
     break
#caso ultrapasse o numero de tentativas
    else:
     print()
     print("login ou senha incorreto") 
     print()
     contador +=1
    if contador==3:
       print("TENTATIVAS DEMAIS, COMPUTADOR BLOQUEADO")
    break
