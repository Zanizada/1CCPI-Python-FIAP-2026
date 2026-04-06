numero = int(input("Digite um número: "))

multiplicador = 0

while multiplicador < 26:
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
    multiplicador += 1