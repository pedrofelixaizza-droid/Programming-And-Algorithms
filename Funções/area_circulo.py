import math


def calcular_area_circulo(raio):
    area = math.pi * (raio**2)
    return area


raio_usuario = float(input("Digite o valor do raio do círculo: "))
area_calculada = calcular_area_circulo(raio_usuario)

print(f"A área do círculo com raio {raio_usuario} é: {area_calculada:.2f}")