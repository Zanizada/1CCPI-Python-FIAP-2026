from functions import conversor_dec

opcao = int(input("Quer converter decimal para outra base, ou de uma base especifica para decimal? (1/2)"))

if opcao == 1:
    numero = int(input("Digite o numero que vai ser convertido: "))
    base = int(input("Digite a base do resultado final: "))

    resultado = conversor_dec(numero, base)
    print(f"O numero {numero} na base {base} eh: {resultado}")