from random import randint

n = int(input("Digite um número inteiro: "))
lista = []

for i in range(n):
    lista.append('')

for i in range(n):
    lista[i] = randint(1, 1000)

print(lista)