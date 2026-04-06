numero = int(input("Digite um número positivo: "))
if numero < 0:
    while numero < 0:
        print("Erro: Número negativo.")
        numero = int(input("Digite um número positivo: "))

numeros = []
for num in range(1, numero):
    numeros.append(num)

print(f"A soma de 1 até {numero} é: {sum(numeros)}")
