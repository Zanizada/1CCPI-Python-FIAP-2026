def aniversario(dia_atual, mes_atual, ano_atual, dia_nascimento, mes_nascimento, ano_nascimento, idade_selecionada=None):
    if idade_selecionada == None:
        idade_atual = ano_atual - ano_nascimento
    else:
        if ano_atual - ano_nascimento == idade_selecionada:
            if mes_nascimento < mes_atual:
                idade_atual = idade_selecionada
            elif mes_nascimento == mes_atual:
                if dia_nascimento <= dia_atual:
                    idade_atual = idade_selecionada
                else:
                    idade_atual = idade_selecionada - 1
            else:
                idade_atual = idade_selecionada - 1
        else:
            idade_atual = ano_atual - ano_nascimento

    return idade_atual

dd, mm, aaaa = map(int, input("Digite sua data de nascimento no formato dd/mm/aaaa: ").split("/"))

dia = 1
mes = 4
ano = 2026

if ano - aaaa == 18:
    idade = aniversario(dia, mes, ano, dd, mm, aaaa, 18)
elif ano - aaaa == 70:
    idade = aniversario(dia, mes, ano, dd, mm, aaaa, 70)
else:
    idade = aniversario(dia, mes, ano, dd, mm, aaaa)

if 18 <= idade < 70:
    print("Voto obrigatório.")
elif 16 <= idade < 18 or idade >= 70:
    print("Voto opcional.")
else:
    print("Voto proibido.")