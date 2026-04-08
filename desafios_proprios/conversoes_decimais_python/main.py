import functions

escolha = int(input("O que deseja fazer?\n1 - Converter decimal para outra base;\n2 - Converter uma base para decimal;\n3 - Converter uma base para outra base.\nEscolha(1/2/3): "))
print()

match escolha:
    case 1:
        numero = int(input("Digite um número: "))
        base = int(input("Digite a base: "))

        print(f"O número {numero} na base {base} é: {functions.decforbase(numero, base)}")
