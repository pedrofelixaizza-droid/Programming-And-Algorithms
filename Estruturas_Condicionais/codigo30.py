salario = float(input("Digite o salário atual: R$ ").replace(',', '.'))

if salario <= 1500.00:
    percentual = 20
elif salario <= 3000.00:
    percentual = 15
else:
    percentual = 10

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print(f"Aumento: {percentual}% (R$ {aumento:.2f})")
print(f"Novo Salário: R$ {novo_salario:.2f}")
