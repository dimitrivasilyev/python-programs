x = int(input("Digite um número: "))
y = int(input("Digite um segundo número: "))
print("""
Como você quer calcular?:
1>: x^y
2>: y^x""")
choose = int(input(':.>'))
if choose == 1:
    print("Resultado:",x**y)
elif choose == 2:
    print("Resultado:",y**x)
else:
    print("ERROR: Houve erro no cálculo.")
