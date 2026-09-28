n1 = float(input("Digite a primeira nota: ").replace(',', '.'))
n2 = float(input("Digite a segunda nota: ").replace(',', '.'))
media = (n1 + n2) / 2

if media >= 7.0:
    print(f"Média {media:.1f}: APROVADO")
elif media >= 5.0:
    print(f"Média {media:.1f}: RECUPERAÇÃO")
else:
    print(f"Média {media:.1f}: REPROVADO")
