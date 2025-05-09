import os

os.system("cls || clear")


def metros_para_centimetros(metros):
    return metros * 100


metros = float(input("Digite um valor em metros: "))


centimetros = metros_para_centimetros(metros)
print(f"{metros} metor equivalem a { centimetros} centimetros.")
