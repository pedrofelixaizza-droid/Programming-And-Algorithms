dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

valida = False

if 1 <= mes <= 12 and ano > 0:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias_no_mes = 31
    elif mes in [4, 6, 9, 11]:
        dias_no_mes = 30
    else:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            dias_no_mes = 29
        else:
            dias_no_mes = 28
    
    if 1 <= dia <= dias_no_mes:
        valida = True

if valida:
    print(f"Data válida: {dia:02d}/{mes:02d}/{ano:04d}")
else:
    print("Data inválida")
