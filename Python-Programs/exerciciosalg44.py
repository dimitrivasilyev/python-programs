salario_bruto = float(input("INSS> Digite o salário bruto: "))
if salario_bruto == 1659.38:
	INSS = salario_bruto/100*8
	print("INSS>:Salário líquido:", INSS)
elif salario_bruto == 1659.39 or 2765.66:
	INSS = salario_bruto/100*9
	print("INSS>:Salário líquido:", INSS)
elif salario_bruto == 2765.67 or 5531.31:
	INSS = salario_bruto/100*11
	print("INSS>:Salário líquido:", INSS)
elif salario_bruto >= 5531.31:
	INSS = salario_bruto-608.44
	print("INSS>:Salário líquido:", INSS)
else:
	print("ERRO: Ocorreu um erro no calculo.")

if salario_bruto == 1903.99 or 2826.65:
	liquido = salario_bruto-INSS-(salario_bruto/100*7.5-142.80)
	print("IRRF>:Salário líquido: {:.4f}".format(liquido))
elif salario_bruto == 2826.66 or 3751.05:
	ir = salario_bruto/100*15-354.80
	liquido = salario_bruto-INSS-ir
	print("IRRF>:Salário líquido: {:.4f}".format(liquido))
elif salario_bruto == 3751.06 or 4664.68:
	ir = salario_bruto/100*22.5-636.13
	liquido = salario_bruto-INSS-ir
	print("IRRF>:Salário líquido: {:.4f}".format(liquido))
elif salario_bruto >= 4664.68:
	ir = salario_bruto/100*27.5-869.36
	liquido = salario_bruto-INSS-ir
	print("IRRF>:Salário líquido: {:.4f}".format(liquido))
