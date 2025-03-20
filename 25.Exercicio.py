import os
os.system("cls || clear")

while True:
    nota1=float(input("digite a primeira nota"))
    print()
    nota2=float(input("digite a primeira nota"))
    print()

    if nota1>= 0 and nota1<= 10 and nota2 >=0 and nota2<=10:

        print(f"as suas notas é {nota1} e {nota2}")
        print()

        media =(nota1=nota2)/2

        print(f" e a sua media aritmetica é: {media}")
        print()
        if media >=7:

            print("_______________aprovado_______________")
            print()
        elif media == 5:

            print("_______________aprovado_______________")
            print()

            
    