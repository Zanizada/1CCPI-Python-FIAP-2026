import msvcrt

def moneyformat(valor):
    return f"R$ {valor:.2f}"

def notasformat(valor): # 180
    lista_notas = []
    notas = [100, 50, 20, 10, 5]
    for nota in notas:
        qntd_notas = valor // nota
        lista_notas.append(f'{qntd_notas} nota(s) de R$ {nota}')
        valor %= nota
    return lista_notas

def input_senha(prompt="Digite sua senha: "):
    print(prompt, end="", flush=True)
    senha = ""

    while True:
        char = msvcrt.getch()

        if char in {b'\r', b'\n'}:  # Enter
            print()
            break
        elif char == b'\x08':  # Backspace
            if len(senha) > 0:
                senha = senha[:-1]
                print("\b \b", end="", flush=True)
        else:
            senha += char.decode("utf-8")
            print("*", end="", flush=True)

    return senha