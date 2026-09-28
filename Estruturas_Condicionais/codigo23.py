peso = float(input("Digite o peso em kg: ").replace(',', '.'))
altura = float(input("Digite a altura em metros: ").replace(',', '.'))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25.0:
    classificacao = "Peso normal"
elif imc < 30.0:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"IMC: {imc:.2f} - {classificacao}")
