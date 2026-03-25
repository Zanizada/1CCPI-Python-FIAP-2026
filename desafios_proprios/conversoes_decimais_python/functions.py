# Função de conversão decimal para outras bases.
def conversor_dec(numero, base_convertida):
    numeros_hex = {
        "0":  "0",
        "1":  "1",
	    "2":  "2",
	    "3":  "3",
        "4":  "4",
        "5":  "5",
        "6":  "6",
        "7":  "7",
        "8":  "8",
        "9":  "9",
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F"
        }
    resto = []

    while numero >= base_convertida:
        resto.append(str(numero % base_convertida))
        numero //= base_convertida
    resto.append(str(numero))

    if base_convertida == 16:
        i = 0
        # Símbolos para numeros acima de 10.
        while i < len(resto):
            resto[i] = numeros_hex[resto[i]]
            i += 1
        resultado = ''.join(resto[::-1])

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
