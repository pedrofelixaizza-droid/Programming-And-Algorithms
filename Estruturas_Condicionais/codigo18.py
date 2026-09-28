n1 = float(input("Digite o primeiro número: ").replace(',', '.'))
n2 = float(input("Digite o segundo número: ").replace(',', '.'))

if n1 > n2:
    print(f"O maior número é: {n1}")
elif n2 > n1:
    print(f"O maior número é: {n2}")
else:
    print("Os números são iguais")
