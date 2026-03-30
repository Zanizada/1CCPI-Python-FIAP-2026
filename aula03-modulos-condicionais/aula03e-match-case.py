escolha_usuario = 0
# 0 > sai do programa
# 1 > entra no programa

match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entrar no programa")
    case _: # Qualquer caractere que não seja 0 ou 1.
        print("Erro!")