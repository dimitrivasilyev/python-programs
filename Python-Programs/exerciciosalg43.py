salario_bruto = float(input("Digite o salário bruto: "))
if salario_bruto == 1659.38:
    salario_liquido = salario_bruto/100*8
    print("Salário líquido:", salario_liquido)
elif salario_bruto == 1659.39 or 2765.66:
    salario_liquido = salario_bruto/100*9
    print("Salário líquido:", salario_liquido)
elif salario_bruto == 2765.67 or 5531.31:
    salario_liquido = salario_bruto/100*11
    print("Salário líquido:", salario_liquido)
elif salario_bruto >= 5531.31:
    salario_liquido = salario_bruto-608.44
    print("Salário líquido:", salario_liquido)
else:
    print("ERRO: Ocorreu um erro no calculo.")
