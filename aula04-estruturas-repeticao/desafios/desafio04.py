valores_recebidos = 1
lista_valores = []

while valores_recebidos < 6:
    numero = int(input("Digite um número: "))
    lista_valores.append(numero)
    valores_recebidos += 1

print(sum(lista_valores))