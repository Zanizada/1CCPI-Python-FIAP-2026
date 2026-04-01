nota01 = float(input("Primeira Nota: "))
nota02 = float(input("Segunda Nota: "))
nota03 = float(input("Terceira Nota: "))
nota04 = float(input("Quarta Nota: "))

notas = [nota01, nota02, nota03, nota04]

nota_media = sum(notas) / len(notas)

print(f"\nMédia final: {nota_media:.1f}")

if nota_media >= 7:
    print("Aprovado.")
elif 5 >= nota_media < 7:
    print("Em recuperação.")
else:
    print("Reprovado.")