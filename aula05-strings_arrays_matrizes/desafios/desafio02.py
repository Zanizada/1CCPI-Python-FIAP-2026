from random import randint

tamanho_turma = int(input("Digite a quantidade de alunos: "))

turma = []

for i in range(tamanho_turma):
    turma.append(randint(0, 10))

media_turma = sum(turma) // len(turma)

acima = 0
abaixo = 0
iguais = 0

for nota in turma:
    if nota > media_turma:
        acima += 1
    elif nota < media_turma:
        abaixo += 1
    else:
        iguais += 1

if acima == 0: acima = "Nenhuma"
if abaixo == 0: abaixo = "nenhuma"
if iguais == 0: iguais = "nenhuma"

print(f"Nota média da turma: {media_turma}")
print(f"{acima} nota(s) acima da média, {abaixo} nota(s) abaixo da média e {iguais} nota(s) iguais a nota média da turma.")