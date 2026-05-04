vetor_nomes = ["Ana", "Lara", "Luiz", "Caio"]
vetor_duplas = []

for i in range(len(vetor_nomes)):
    for j in range(i+1, len(vetor_nomes)):
        vetor_duplas.append(f"{vetor_nomes[i]} e {vetor_nomes[j]}")

for dupla in vetor_duplas:
    print(dupla)