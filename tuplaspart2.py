print("2. ACESSANDO ELEMENTOS:\n")

tupla = ("P", "E", "D", "R", "O")
print(f"Tupla: {tupla}\n")

print(f"Primeiro elemento: {tupla[0]}")
print(f"Último elemento: {tupla[-1]}")
print(f"Índice 2: {tupla[2]}")
print(f"Índice -2: {tupla[-2]}\n")

print("="*60 + "\n")



print("3. TUPLAS SÃO IMUTÁVEIS:\n")

tupla = ("Pedro Felix", 47803610870, "pedrofelix@gmail.com")
print(f"Tupla original: {tupla}\n")

print("Tentando modificar:")
try:
    tupla[0] = "João"
except TypeError as e:
    print(f" Erro: {e}\n")

print("Tentando trocar valores:")
try:
    tupla.append(4)
except AttributeError as e:
    print(f" Erro: Tuplas não têm append\n")

print("Tuplas são imutáveis (proteção de dados)")
print("Listas podem ser modificadas\n")

print("="*60 + "\n")


# 4. Fatiamento de tuplas
print("4. FATIAMENTO DE TUPLAS:\n")

tupla = ("p", "e", "d", "r", "o", "f", "e", "l", "i", "x")
print(f"Tupla: {tupla}\n")

print(f"tupla[2:5]: {tupla[2:5]}")
print(f"tupla[:3]: {tupla[:3]}")
print(f"tupla[6:]: {tupla[6:]}")
print(f"tupla[::2]: {tupla[::2]}")
print(f"tupla[::-1]: {tupla[::-1]}\n")

print("="*60 + "\n") 


