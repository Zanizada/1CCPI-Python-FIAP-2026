numero = int(input("Digite um número positivo: "))
if numero < 0:
    while numero < 0:
        print("Erro: Número negativo.")
        numero = int(input("Digite um número positivo: "))

numeros = []
for num in range(1, numero + 1):
    if numero % num == 0:
        numeros.append(str(num))

print(f"Os divisores de {numero} são: {", ".join(numeros)}.")
