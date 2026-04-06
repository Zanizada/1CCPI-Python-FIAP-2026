def preco_kg(codigo):
    if 10 <= codigo <= 20:
        preco_p_kg = 100.00
    elif 21 <= codigo <= 30:
        preco_p_kg = 250.00
    else:
        preco_p_kg = 340.00

    return preco_p_kg

impostos = {
    1: 0.35,
    2: 0.25,
    3: 0.15,
    4: 0.05,
    5: 0.00
}

codigo_estado = int(input("Digite o código do estado de origem da carga do caminhão (de 1 a 5): "))
carga_ton = float(input("Digite o valor da carga em toneladas (T): "))
codigo_carga = int(input("Digite o código da carga (de 10 a 40): "))

carga_kg = carga_ton * 1000
preco_p_kg = preco_kg(codigo_carga)
valor_s_imposto = preco_p_kg * carga_kg
imposto = valor_s_imposto * impostos[codigo_estado]
valor_total = valor_s_imposto - imposto

print(f"Peso da carga em Kg: {carga_kg:.2f}")
print(f"Preço da carga do caminhão: R$ {valor_s_imposto:.2f}")
print(f"Valor do imposto: R$ {imposto:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")