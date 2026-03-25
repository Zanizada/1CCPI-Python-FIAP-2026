# Função de conversão decimal para outras bases.
def conversor_dec(numero, base_convertida):
    resto = []

    while numero >= base_convertida:
        resto.append(str(numero % base_convertida))
        numero //= base_convertida
    resto.append(str(numero))

    # Símbolos para números acima de 10.
    if base_convertida > 10:
        i = 0
        while i < len(resto):
            if resto[i] > 35:
                resto[i] = chr((61+resto[i]))
            else:
                resto[i] = chr((55+resto[i]))
            i += 1
        resultado = ''.join(resto[::-1])

    # Formatação da saída do programa para número binário/hex (4 bits)
    elif base_convertida == 2:
        while len(resto) % 4 != 0:
            resto.append("0")
        resultado = ''.join(resto[::-1])
        resultado = [resultado[i:i + 4] for i in range(0, len(resultado), 4)]
        resultado = ' '.join(resultado)

    else:
        resultado = ''.join(resto[::-1])

    return resultado

# Função de conversão de número binário para decimal.
def conversor_bin(binario):
    binario = str(binario)
    numeros = []
    index = 0

    if len(binario) % 4 != 0:
        while len(binario) % 4 != 0:
            binario = "0" + binario

    for numero in binario:
        numeros.append(int(numero))

    # for numero in numeros:

    return 0