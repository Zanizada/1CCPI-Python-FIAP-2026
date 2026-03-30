idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não pode votar!")
elif 16 <= idade < 18 or idade > 70:
    print("Pode votar!")
else:
    print("Deve votar!")