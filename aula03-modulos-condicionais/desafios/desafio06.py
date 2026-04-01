numero01 = int(input("Digite o primeiro número: "))
operador = str(input("Digite o operador: "))
numero02 = int(input("Digite o segundo número: "))

match operador:
    case "+":
        print(numero01 + numero02)
    case "-":
        print(numero01 + numero02)
    case "*":
        print(numero01 * numero02)
    case "/":
        print(numero01 / numero02)