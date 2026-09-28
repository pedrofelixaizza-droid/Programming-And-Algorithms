n1 = float(input("Digite o primeiro número: ").replace(',', '.'))
operador = input("Digite a operação (+, -, *, /): ").strip()
n2 = float(input("Digite o segundo número: ").replace(',', '.'))

if operador == '+':
    print(f"Resultado: {n1 + n2}")
elif operador == '-':
    print(f"Resultado: {n1 - n2}")
elif operador == '*':
    print(f"Resultado: {n1 * n2}")
elif operador == '/':
    if n2 != 0:
        print(f"Resultado: {n1 / n2}")
    else:
        print("Erro: Divisão por zero")
else:
    print("Operador inválido")
