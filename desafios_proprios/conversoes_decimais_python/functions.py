from tabelas import BIN_HEX, BIN_OCT, BIN_QUATRO

# Função para formatar string em lista.
def string_lista(string):
    lista = []
    for s in string:
        lista.append(s)
    return lista

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

# Função de identificação de base.
def base(numero, base_num):
    binario = []
    bins = {
        4:  BIN_QUATRO,
        8:  BIN_OCT,
        16: BIN_HEX
    }
    dicio = bins[base_num]

    i = 0
    while i < len(numero):
        binario.append(dicio[numero[i]])
        i += 1

    return binario

# Função de conversão de número de base por bit (2, 4, 8, 16).
def conversor_bin(numero, base_um, base_dois):
    numero = string_lista(numero)
    binario = base(numero, base_um)
