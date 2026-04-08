import functions, time

print("Bem-vindo ao seu caixa eletrônico.\n")

attempts = 1

while True:
    login = input(f"Insira a sua senha ({4-attempts} tentativas restantes): ")
    if attempts >= 3:

        for i in range(300, 0, -1):
            minutos = i // 60
            segundos = i - (minutos * 60)
            print(f"\rConta bloqueada, tente novamente em {minutos} minutos e {segundos} segundos", end="")
            time.sleep(0.01)

        print("\nConta liberada.\n")
        attempts = 1
        continue

    if login == "simuladorATM2026":
        print("Login bem-sucedido!\n")
        break
    else:
        attempts += 1

saldo = 1000.00
depositos = []
saques = []

while True:
    escolha = int(input("1 - Ver saldo\n2 - Depositar\n3 - Sacar\n4 - Histórico\n5 - Sair\nEscolha: "))

    match escolha:
        case 1: # Saldo
            print(f"\nSaldo: {functions.moneyformat(saldo)}\n")
            continue
        case 2: # Depositar
            deposito = float(input("Insira o valor do depósito: "))
            saldo += deposito
            depositos.append(f"Depósito: {functions.moneyformat(deposito)}")
            print(f"\nDepósito de {functions.moneyformat(deposito)} concluído.\nSaldo: {functions.moneyformat(saldo)}")
            continue
        case 3: # Sacar
            saque = int(input("Insira o valor do saque desejado: "))

            if saque % 5 != 0:
                print("Sáque inválido, tente novamente.")
                saque = int(input("Insira o valor do saque desejado: "))

            notas = functions.notasformat(saque)
            notas = "\n".join(notas)
        # case 4: # Histórico

        case 5: # Sair
            print("\nFim.\n")
            break