from tabelas import BIN_HEX, BIN_OCT, BIN_QUATRO, bins, bits

# Função para formatar string em lista.
def string_lista(string):
    return list(string)

# Função de conversão decimal para outras bases.
def conversor_dec(numero, base_convertida):
    resto = []

    while numero >= base_convertida:
        resto.append(str(numero % base_convertida))
        numero //= base_convertida
    resto.append(str(numero))

    # Símbolos para números acima de 10.
    if base_convertida > 10:
        for i in range(len(resto)):
            valor = int(resto[i])
            if valor >= 10:
                resto[i] = chr(55 + valor)
            else:
                resto[i] = str(valor)

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
    dicio = bins[base_num]

    i = 0
    while i < len(numero):
        binario.append(dicio[numero[i]])
        i += 1

    return binario

def separacao_bits(base, binario):
    novo_bin = []
    novo_bin_2 = []
    bit_destino = bits[base]

    binario = ''.join(binario)
    binario = list(binario)
    i = 0
    bit = 1

    while i < len(binario):

        if bit == 3:
            novo_bin = ''.join(novo_bin)
            novo_bin_2.append(novo_bin)
            novo_bin = []
            bit = 1

    novo_bin.append(binario[i])
    i += 1
    bit += 1

# Função de conversão de número de base por bit (2, 4, 8, 16).
def conversor_bin(numero, base_um, base_dois):
    numero = string_lista(numero)
    binario = base(numero, base_um)

    if base_dois == 2:
        resultado = ' '.join(binario)

    elif base_dois == 4:
