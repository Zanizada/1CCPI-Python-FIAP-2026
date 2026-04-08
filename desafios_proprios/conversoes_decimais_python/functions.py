import tabelas

# FUNÇÕES SECUNDÁRIAS

def strformat(numero):
    if numero >= 10:
        return chr(55+numero)
    else:
        return str(numero)

def numformat(string):
    numeros = []
    for num in string:
        if ord(num) >= 65:
            numeros.append(ord(num) - 55)
        else:
            numeros.append(int(num))
    return numeros[::-1]

def resultformat(lista):
    lista = lista[::-1]
    return "".join(lista)

def bitsbase(base):
    match base:
        case 16:
            return 4
        case 8:
            return 3
        case 4:
            return 2
    return None

# FUNÇÕES PRINCIPAIS

def decforbase(numero, base):
    numeros = []

    while numero > 1:
        numeros.append(numero % base)
        numero //= base
    if numero == 1:
        numeros.append(1)

    resultado = []

    for num in numeros:
        resultado.append(strformat(num))

    return resultformat(resultado)

def basefordec(numero, base):
    numero = numformat(numero)
    numeros = []

    for i in range(0, len(numero)):
        operacao = numero[i] * (base**i)
        if operacao != 0:
            numeros.append(operacao)

    return sum(numeros)

def baseforbase(numero, base_inicio, base_fim): # "4AF", 16, 8
    dic_base_inicio = tabelas.BITS[bitsbase(base_inicio)] # dbi = BIN_HEX
    dic_base_fim = tabelas.BITS[bitsbase(base_fim)] # dbf = BIN_OCT
    bits = bitsbase(base_fim) # bits = 3

    numeros = []
    for num in numero: # 4AF
      numeros.append(dic_base_inicio[num]) # "4" --> "0100", "A" --> "1010", "F" --> "1111"
    # numeros = ["0100", "1010", "1111")
    numeros = "".join(numeros) # 010010101111

    resto = len(numeros) % bits # 3 % 3 = 0
    if resto != 0:
        numeros = "0" * (bits - resto) + numeros # "0" à esquerda da string

    partes = []
    for i in range(0, len(numeros), bits):
        pedaco = numeros[i:i+bits]
        partes.append(pedaco)
    # partes = ["010", "010", "101", "111"]
    numeros = []
    for num in partes:
        numeros.append(dic_base_fim[num]) # "010" = "2", "010" = "2", "101" = 5, "111" = 7
    # numeros = ["2", "2", "5", "7"]

    return "".join(numeros)