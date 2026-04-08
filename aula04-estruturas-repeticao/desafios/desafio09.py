def primo(numero):
    divisores = []
    for num in range (1, numero+1):
        if numero % num == 0:
            divisores.append(num)
    if len(divisores) == 2:
        return True
    else:
        return False

for num in range(2, 2000):
    if primo(num):
        print(num)
    else:
        continue