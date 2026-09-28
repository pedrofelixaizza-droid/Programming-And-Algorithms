entrada = input("Digite um número: ").replace(',', '.')
numero = float(entrada)

if numero > 0:
    resultado = "POSITIVO"
elif numero < 0:
    resultado = "NEGATIVO"
else:
    resultado = "ZERO"

print(f"Resultado: {resultado}")
