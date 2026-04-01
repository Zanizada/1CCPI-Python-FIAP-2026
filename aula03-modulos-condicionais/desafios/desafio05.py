A = int(input())
B = int(input())

if A < B:
    A, B = B, A

if A % B == 0:
    print("São Múltiplos.")
else:
    print("Não são Múltiplos.")