a = float(input("Digite o lado A: ").replace(',', '.'))
b = float(input("Digite o lado B: ").replace(',', '.'))
c = float(input("Digite o lado C: ").replace(',', '.'))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os lados não formam um triângulo válido")
