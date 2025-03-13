import os
os.system("clear")

#// processamento.
dia_semana = int(input("Escreva o dia da semano em numero ( de 1' A 7)"))


match dia_semana:
    case 1:
        dia_escrito = "segunda-feira"
        dia_utilidade = "Dia util"
    case 2:
        dia_escrito = "terça-feira"
        dia_utilidade = "Dia util"
    case 3:
        dia_escrito = "Quarta-feira"
        dia_utilidade = "Dia util"
    case 4:
        dia_escrito = "Quinta-feira"
        dia_utilidade = "Dia util"
    case 5:
        dia_escrito = "Sexta=feira"
        dia_utilidade = "Dia util"
    case 6:
        dia_escrito = "Sabado"
        dia_utilidade = "final de semana"
    case 7:
        dia_escrito = "Domingo"
        dia_utilidade = "final de semana"
    case _: 
        dia_escrito = "invalido"
        dia_utilidade = 0


#// Saída. 
print()
print(f"{dia_escrito}")
print(F"{dia_utilidade}")