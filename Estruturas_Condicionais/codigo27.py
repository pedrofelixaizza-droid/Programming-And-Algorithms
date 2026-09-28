n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n2 != 0 and n1 % n2 == 0:
    print(f"{n1} é múltiplo de {n2}")
elif n2 == 0:
    print("Não é possível verificar múltiplos com zero")
else:
    print(f"{n1} não é múltiplo de {n2}")
