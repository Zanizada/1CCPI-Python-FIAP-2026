vetor_nomes = ["Rafael", "Fernando", "Felipe", "João"]
vetor_duplas = [["vazio", ""]]
duplas_formadas = []

for i in range(len(vetor_nomes)):
    for j in range(len(vetor_nomes)):
        if i != j:
            vetor_duplas.append([vetor_nomes[i],vetor_nomes[j]])

for i in range(len(vetor_nomes)):
    for j in range(len(vetor_nomes)):
        if vetor_duplas[i][0] != "vazio":
            if vetor_nomes[i] != vetor_nomes[i][0]:
                duplas_formadas.append(vetor_duplas[i])
            elif vetor_nomes[i] != vetor_nomes[i][0] and vetor_nomes[i] != vetor_nomes[i][1]:
                duplas_formadas.append(vetor_duplas[i])
        # i = 0
        # j = 0
        # vetor_duplas[1][0] == "Rafael"
        # vetor_nomes[1] == "Rafael
        # duplas_formadas = [["Rafael", "Fernando"]]

print(vetor_nomes)
print()
print(vetor_duplas)
print()
print(duplas_formadas)