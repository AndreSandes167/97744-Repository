# 1 - Limpando o terminal.
import osos.system("clear")

# 2 - Solicitando dados para o usuário.
valor_produto = float(input("Digite o valor do produto: "))


print("""
======================= FORMA DE PAGAMENTO ===================
      
1    \ tA vista
2     \ tA prazo
""")
forma_de_pagamento = int(input("Digite a forma de pagamento: "))

#  3 - verificando.
match forma_de_pagamento:
      case 1:
          # Obtendo o valor do desconto de (10%)")
          desconto = valor_produto - 0.10
          
      case 2:
          parcelas = int(input("Digite a quantidade de parcelas: "))
          
      case _:
          print("Opção inválida.")

          # 4 - Exibindo resultados."
          print()