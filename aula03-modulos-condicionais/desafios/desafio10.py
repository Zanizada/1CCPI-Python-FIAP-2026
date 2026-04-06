A, B, C = map(int, input("Digite os lados A, B e C do triângulo: ").split())

if A == B == C:
    resultado = "TRIANGULO EQUILATERO"
elif A == B or A == C or B == C:
    resultado = "TRIANGULO ISOSCELES"
else:
    lados = [A, B, C]
    lados.sort(reverse=True)
    A, B, C = lados[0], lados[1], lados[2]
    if A >= B + C:
        resultado = "NAO FORMA TRIANGULO"
    elif A**2 == B**2 + C**2:
        resultado = "TRIANGULO RETANGULO"
    elif A**2 > B**2 + C**2:
        resultado = "TRIANGULO OBTUSANGULO"
    elif A**2 < B**2 + C**2:
        resultado = "TRIANGULO ACUTANGULO"

print(resultado)