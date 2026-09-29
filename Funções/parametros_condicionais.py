def encontrar_maior(a, b, c):
  if a >= b and a >= c:
    return a
  elif b >= a and b >= c:
    return b
  else:
    return c


num1 = int(input("Introduza o primeiro número inteiro: "))
num2 = int(input("Introduza o segundo número inteiro: "))
num3 = int(input("Introduza o terceiro número inteiro: "))

maior = encontrar_maior(num1, num2, num3)
print(f"O maior número é: {maior}")
