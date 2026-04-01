def reajuste_salarial(salario):
    if salario <= 280.00:
        percentual = 0.20
    elif 280.00 < salario <= 700.00:
        percentual = 0.15
    elif 700.00 < salario <= 1500.00:
        percentual = 0.10
    else:
        percentual = 0.05

    return percentual

salario_atual = float(input("Informe o seu salário atual: "))
percentual_de_aumento = reajuste_salarial(salario_atual)
aumento = salario_atual * percentual_de_aumento
salario_novo = salario_atual + aumento

print(f"Salário anterior ao reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento salarial: {int(percentual_de_aumento*100)}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário depois do reajuste: R$ {salario_novo:.2f}")
