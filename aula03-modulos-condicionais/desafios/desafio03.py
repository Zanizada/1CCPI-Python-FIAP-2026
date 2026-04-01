numero01 = int(input("Digite o primeiro número: "))
numero02 = int(input("Digite o segundo número: "))

if numero01 == numero02:
    print("Os dois números são iguais.")
elif numero01 > numero02:
    print(f"O número {numero01} é maior.")
else:
    print(f"O número {numero02} é maior.")