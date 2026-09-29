import math


def calcular_hipotenusa(cateto_a, cateto_b):
  return math.sqrt(cateto_a**2 + cateto_b**2)


cateto_a = float(input("Introduza a medida do primeiro cateto: "))
cateto_b = float(input("Introduza a medida do segundo cateto: "))

hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)
print(f"A hipotenusa do triângulo retângulo é: {hipotenusa:.2f}")