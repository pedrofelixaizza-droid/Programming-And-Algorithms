quantidade = int(input("Digite a quantidade comprada: "))
preco_unitario = float(input("Digite o preço unitário: R$ ").replace(',', '.'))

valor_total = quantidade * preco_unitario

if quantidade > 10:
    desconto = valor_total * 0.10
elif quantidade >= 5:
    desconto = valor_total * 0.05
else:
    desconto = 0.0

valor_final = valor_total - desconto

print(f"Valor total: R$ {valor_total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")
