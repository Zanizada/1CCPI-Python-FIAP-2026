numero = int(input("Digite um número: "))
pares = []

for num in range(2, numero):
    if num % 2 == 0:
        pares.append((num))

print(pares)