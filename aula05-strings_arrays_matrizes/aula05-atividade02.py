matriz = [
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', '']
]
numero = 1

for i in range(4):
    for j in range(5):
        matriz[i][j] = numero
        numero += 1

for i in range(4):
    print(matriz[i])