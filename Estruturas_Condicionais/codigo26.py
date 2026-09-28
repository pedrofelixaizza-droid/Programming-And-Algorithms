letra = input("Digite uma letra: ").strip().lower()

if len(letra) == 1 and letra.isalpha():
    if letra in "aeiou":
        print("Vogal")
    else:
        print("Consoante")
else:
    print("Entrada inválida")
