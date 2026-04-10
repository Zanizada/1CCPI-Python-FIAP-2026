import functions, time

""" print("Bem-vindo ao seu caixa eletrônico.\n")

attempts = 0

while True:
    login = functions.input_senha(f"Insira a sua senha ({4-attempts} tentativas restantes): ")
    if attempts > 2:

        for i in range(300, 0, -1):
            minutos = i // 60
            segundos = i - (minutos * 60)
            print(f"\rConta bloqueada, tente novamente em {minutos} minutos e {segundos} segundos", end="")
            time.sleep(1)

        print("\nConta liberada.\n")
        attempts = 1
        continue

    if login == "simuladorATM2026":
        print("Login bem-sucedido!\n")
        break
    else:
        attempts += 1 """

saldo = 1000.00
saques = 0
historico = []
tempo = 24

while True:
    escolha = int(input("\n1 - Ver saldo\n2 - Depositar\n3 - Sacar\n4 - Histórico\n5 - Sair\nEscolha: "))

    match escolha:
        case 1: # Saldo
            print(f"\nSaldo: {functions.moneyformat(saldo)}")

        case 2: # Depositar
            deposito = float(input("\nInsira o valor do depósito: "))
            saldo += deposito
            historico.append(f"Depósito: {functions.moneyformat(deposito)}")
            print(f"\nDepósito de {functions.moneyformat(deposito)} realizado.")

        case 3: # Sacar
            if saques > 2:
                print(f"Limite de saques diários atingidos.\n")
            else:
                print(f"\nMáximo de 3 saques por dia.")
                print(f"Saques realizados hoje: {saques}")
                saque = int(input("Insira o valor do saque desejado: "))
                if saque % 5 != 0:
                    print("\nSáque inválido, tente novamente.")
                    saque = int(input("Insira o valor do saque desejado: "))
                saldo -= saque
                saques += 1
                historico.append(f"Saque: {functions.moneyformat(saque)}")
                notas = functions.notasformat(saque)
                notas = "\n".join(notas)
                print(f"\nSaque de R$ {(saque)} realizado.")
                print(notas)

        case 4: # Histórico
            print(f"\n{"\n".join(historico)}")

        case 5: # Sair
            print("\nFim.\n")
            exit()