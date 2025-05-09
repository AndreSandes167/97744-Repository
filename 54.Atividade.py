import os

from dataclasses import dataclass

os.system("cls || clear ")

def solicitar_dados_carro (numero):
    print(f"\nDigite os dados do carro {numero}:")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    categoria = input("Categoria: ")
    preço = input("preço:")
    return f"carro {numero}:\nMarca: {marca}\nModelo: {modelo}\ncategoria: {categoria}"

def main():
    carro1 = solicitar_dados_carro(1)
    carro2 = solicitar_dados_carros(2)

    with open("carros.txt"), "w", encoding="utf-8") as arquivo:
arquivo.write(carro1 + "\n")
arquivo.write(carro2 + "\n")


print("\nos dados dos carros foram salvos em 'carros.txt'.")

if __name__ == "__main__":
    main()