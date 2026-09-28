nota = float(input("Digite a nota (0 a 10): ").replace(',', '.'))

if 9.0 <= nota <= 10.0:
    print("Conceito A")
elif 7.5 <= nota < 9.0:
    print("Conceito B")
elif 6.0 <= nota < 7.5:
    print("Conceito C")
elif 4.0 <= nota < 6.0:
    print("Conceito D")
elif 0.0 <= nota < 4.0:
    print("Conceito F")
else:
    print("Nota inválida")
