def moneyformat(valor):
    return f"R$ {valor:.2f}"

def notasformat(valor): # 180
    lista_notas = []
    notas = [100, 50, 20, 10, 5]
    for nota in notas:
        qntd_notas = valor // nota
        lista_notas.append(f'{qntd_notas} nota(s) de R$ {nota}.00')
        valor %= nota
    return lista_notas