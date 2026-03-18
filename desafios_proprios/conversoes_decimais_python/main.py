from functions import conversor

numero = int(input("Digite o numero que vai ser convertido: "))
base = int(input("Digite a base do resultado final: "))

resultado = conversor(numero, base)
print(f"O numero {numero} na base {base} eh: {resultado}")