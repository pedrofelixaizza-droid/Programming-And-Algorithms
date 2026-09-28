num = float(input("Digite um número: ").replace(',', '.'))
inicio = float(input("Digite o início do intervalo: ").replace(',', '.'))
fim = float(input("Digite o fim do intervalo: ").replace(',', '.'))

if inicio <= num <= fim:
    print(f"O número {num} está dentro do intervalo [{inicio}, {fim}]")
else:
    print(f"O número {num} está fora do intervalo [{inicio}, {fim}]")
